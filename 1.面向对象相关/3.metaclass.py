#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-21 16:31
# File    : 3.metaclass.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
# 创建类的两种方式;

# 方式一：
class Foo(object):
    CITY = 'BJ'

    def func(self, x):
        return x + 1


# 方式二：

def func(self, x):
    return x + 1


# Foo1 = type('Foo1', (object,), {'CITY': 'BJ', 'func': func})


# 另外一种形式:
Foo2 = type('Foo', (object,), {'CITY': 'BJ', 'func': lambda self, x: x + 1})


# 2、类由自定义type创建；
class Foo3(object, metaclass=type):  # 当前类由type类创建;
    # __metaclass__ = type# Python2的创建方式;
    CITY = 'BJ'

    def func(self, x):
        return x + 1


class MyType(type):
    def __init__(self, *args, **kwargs):
        print('创建类之前')
        super(MyType, self).__init__(*args, **kwargs)
        print('创建类之后')


class Foo4(object, metaclass=MyType):
    CITY = 'BJ'

    def func(self, x):
        return x + 1


print(Foo4)
"""
1、类由type创建，metaclass可以指定当前类由哪一个类创建;
"""


class MyType1(type):
    def __init__(self, *args, **kwargs):
        print('创建类之前')
        super(MyType1, self).__init__(*args, **kwargs)
        print('创建类之后')


class Foo1(object, metaclass=MyType1):
    CITY = 'BJ'

    def func(self, x):
        return x + 1


class Bar(Foo):
    pass


"""
小结：
1、默认类由type实例化创建；
2、某个类指定metaclass = MyType，那么当前类的所有派生类都由于MyType创建；
3、实例化对象：
    -type.__init__
    -type.__call__
    -类名.__new__
    -类名.__init__
"""
