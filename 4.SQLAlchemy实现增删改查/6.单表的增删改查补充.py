#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 15:38
# File    : 6.单表的增删改查补充
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import models

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
maker = sessionmaker(engine)

session = maker()

# 查询补充操作；
# 1、label起个别名;
result = session.query(models.Classes.id, models.Classes.name.label('alias')).all()
print(result)  # [(1, '全栈1期999'), (2, '全栈2期999'), (13, '全栈3期999')]
for item in result:
    print(item.id, item.alias)
    # print(item.id,item.name)
# print(item[0],item[1])
# print(item,type(item),item.id,item.name)
# 尾部的参数决定了是进行字符串操作还是数学运算操作；

# 2、 filter和filter_by;
r3 = session.query(models.Classes).filter(models.Classes.name == "cui").all()
r4 = session.query(models.Classes).filter_by(name="cui").all()
print(r3, r4)

# 3、子查询操作；
r5 = session.query(models.Classes).from_statement(text("SELECT * FROM classes where name = :name")).params(name="ed")
print(r5)  # SELECT * FROM classes where name = %(name)s

session.commit()
session.close()
