#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 15:29
# File    : 3.单表的查询操作.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")

maker = sessionmaker(bind=engine)
session = maker()
# 查询;

result = session.query(models.Classes).all()
# print(result)#[<models.Classes object at 0x10dcb2358>, <models.Classes object at 0x10dcb23c8>, <models.Classes object at 0x10dcb2438>, <models.Classes object at 0x10dcb24a8>, <models.Classes object at 0x10dcb2518>]
for item in result:
    print(item.id, item.name)
session.commit()
session.close()
