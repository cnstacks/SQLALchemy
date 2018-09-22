#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-21 16:26
# File    : 1.mro.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
class Foo(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    CITY = 'BJ'

    def func(self):
        pass


print(
    Foo.__dict__)  # {'__module__': '__main__', 'CITY': 'BJ', 'func': <function Foo.func at 0x107b96268>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
print(Foo.CITY)  # BJ
print(Foo.func)  # <function Foo.func at 0x107b96268>


obj1 = Foo('cuixiaozhao',26)
print(obj1.__dict__)#{'age': 'cuixiaozhao', 'name': 26}