# -*- coding:utf-8 -*-
__author__ = 'wendong'


class QiYU(object):
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = "male"

    def keys(self):
        return ['name', 'age', 'gender']

    def __getitem__(self, item):
        return getattr(self, item)
o = QiYU()
print(o['name'])
print(o['age'])
print(dict(o))


