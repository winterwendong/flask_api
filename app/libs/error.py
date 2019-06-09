# -*- coding:utf-8 -*-

from flask import request, json

__author__ = 'wendong'


from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake (∩_∩)'
    # 未知错误
    status_code = 999

    def __init__(self, msg=None, code=None, status_code=None, headers=None):

        if code:
            self.code = code
        if status_code:
            self.status_code = status_code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            status_code = self.status_code,
            request = request.method + ' ' + self.get_url_no_parma()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """GET a list of header."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_parma():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

