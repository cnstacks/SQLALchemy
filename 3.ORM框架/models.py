#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 09:54
# File    : models.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
1、安装pip3 install sqlalchemy ；
2、依赖于pymysql进行数据库连接；
3、并不支持修改表结构，仅支持在数据库修改字段后，再重新在此处修改；
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index
from sqlalchemy import create_engine

Base = declarative_base()


# 创建数据表;
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    extra = Column(String(16))

    # __table_args = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra')
    # )

# 数据库连接相关；
# engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com/flask_session?charset=utf8")
# Base.metadata.create_all(engine)
# 删除表;
#Base.metadata.drop_all(engine)

# 向表中插入数据；
