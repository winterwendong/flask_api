# -*- coding:utf-8 -*-
from app.libs.error_code import DeleteSuccess, AuthFailed
from app.models.base import db
from app.models.user import User

__author__ = 'wendong'
from flask import Blueprint, jsonify, g
from app.libs.redprint import  Redprint
from app.libs.token_auth import auth

# user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    scope = g.user.scope
    if not scope:
        raise AuthFailed()
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('/', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 超权
    uid = g.user.uid
    # g变量是线程隔离的
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

