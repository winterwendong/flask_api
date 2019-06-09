# -*- coding:utf-8 -*-
from flask import request

from app.libs.error_code import ClientTypeError, Success
from app.models.user import User
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, ClientTypeEnum, UserEmailForm

api = Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email
    }
    # 二次开发
    promise[form.type.data]()
    # 我们可以预知的异常，已知异常 APIException
    # 我们完全没有意识到异常 未知异常

    # 我们可以接受定义时的复杂，但不能接受调用时的复杂
    # AOP思想
    return Success()
    # 注册 登录
    # 参数校验 接受参数
    # WTForms 验证表单

def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)