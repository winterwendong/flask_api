# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'wendong'


class Success(APIException):
    code = 201
    msg = 'ok'
    status_code = 0


class DeleteSuccess(APIException):
    code = 202
    msg = 'ok'
    status_code = -1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake (∩_∩)'
    status_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    status_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    status_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0__0...'
    status_code = 1001


class AuthFailed(APIException):
    # 授权失败
    code = 401
    msg = 'authorization failed'
    status_code = 1005


class Forbidden(APIException):
    # 禁止访问 权限不够 或者就是不让你访问
    code = 403
    status_code = 1004
    msg = 'forbidden, not in scope'


class DuplicateGift(APIException):
    code = 400
    status_code = 2001
    msg = 'the current book has already in gift'