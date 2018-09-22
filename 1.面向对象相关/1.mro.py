#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-21 16:26
# File    : 1.mro.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
class A(object):
    pass


class B(A):
    pass


class C(object):
    pass


class D(B, C):
    pass


print(
    D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)
"""
1、__mro__，显示当前类查找属性的顺序；
"""
