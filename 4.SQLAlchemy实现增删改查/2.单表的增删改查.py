#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 15:14
# File    : 2.单表的增删改查.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
xxxx = sessionmaker(bind=engine)
session = xxxx()


# 增加
obj = models.Classes(name = "全栈1期")
session.add(obj)



session.commit()
session.close()