# -*- coding:utf-8 -*-
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

from app.libs.error_code import AuthFailed

__author__ = 'wendong'

from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, TokenForm
from app.libs.enums import  ClientTypeEnum
from app.models.user import User

api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verity,
    }

    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    t = {
        "token": token.decode('ascii')
    }
    return jsonify(t), 201


@api.route('/secret',methods=['POST'])
def get_token_info():
    """获取令牌信息"""
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', status_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is expired', status_code=1002)
    r = {
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    }
    return jsonify(r)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        "uid": uid,
        "type": ac_type.value,
        "scope": scope
    })