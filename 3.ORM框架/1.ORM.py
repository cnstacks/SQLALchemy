#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 09:54
# File    : 1.ORM.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

""
"""
SQLAlchemy插入数据操作；
"""
import models
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

obj1 = models.Users(name="cuixiaozhao", extra="cxz")
obj2 = models.Users(name="cuixiaozhao", extra="cxz")


session.add(obj1)
session.add(obj2)
session.commit()
