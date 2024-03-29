# -*- coding:utf-8 -*-
from app.libs.error import APIException, HTTPException
from app.libs.error_code import ServerError

__author__ = 'wendong'
from app import create_app

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        status_code = 1007
        return APIException(msg, code, status_code)
    else:
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e



if __name__ == '__main__':
    app.run(debug=True)