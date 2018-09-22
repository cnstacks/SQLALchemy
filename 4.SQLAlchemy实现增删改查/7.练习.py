#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 16:15
# File    : 7.练习.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import models

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")

maker = sessionmaker(bind=engine)
session = maker()
obj = models.Student(username='崔晓丝', password='123456', class_id=2)
session.add(obj)

# 在学生表中找到崔晓丝;
obj1 = session.query(models.Student).filter(models.Student.username == '崔晓丝').first()
print(obj1)  # <models.Student object at 0x108762a90>

# 找到所有学生;
# 1、LOW B查询方式；
# objs = session.query(models.Student).all()
# for obj in objs:
#     cls_obj = session.query(models.Classes).filter(models.Classes.id ==obj.class_id).first()
#     print(obj.id,obj.username,obj.class_id,cls_obj.name)
# 2、主动连表操作；
objs = session.query(models.Student.id, models.Student.username, models.Classes.name).join(models.Classes,                                                                                        isouter=True).all()
print(objs)

# 3、relationship引入；
objs2 = session.query(models.Student).all()
for item in objs2:
    print(item.id,item.username,item.class_id,item.cls.name)

session.commit()
session.close()


# 4、全栈2期所有的学生
obj3 = session.query(models.Classes).filter(models.Classes.name =="全栈2期999").first()

student_list = obj3.stus
for i in student_list:
    print(i.id,i.username)
print("全栈2期所有的学生",student_list)

