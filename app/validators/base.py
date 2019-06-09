# -*- coding:utf-8 -*-
from flask import request

from app.libs.error_code import ParameterException

__author__ = 'wendong'

from wtforms import Form

class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(self.errors)
        return self