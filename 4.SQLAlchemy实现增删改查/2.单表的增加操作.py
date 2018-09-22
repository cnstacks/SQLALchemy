#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 15:14
# File    : 2.单表的增加操作.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
xxxx = sessionmaker(bind=engine)
session = xxxx()

# 单条记录增加
# obj = models.Classes(name = "全栈1期")
# session.add(obj)

# 多条记录增加；
objs = [
    # models.Classes(name = '全栈2期'),
    models.Classes(name='全栈3期'),
    models.Classes(name='全栈4期'),
    models.Classes(name='全栈5期'),
]
session.add_all(objs)
session.commit()
session.close()
