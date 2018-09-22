#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 19:10
# File    : 1.总结.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

# import models
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
# xxxx = sessionmaker(bind=engine)
# session = xxxx()
#
# session.add
# session.add_all()
# session.query(Users).all()
# session.query(Users.id, Users.name).filter(User.name == 'alex')
# session.query(Users.id, Users.name).filter_by(name='alex')
# session.query(Users.id, Users.name).filter_by(name='alex').filter()
#
# session.query(Users.id, Users.name).filter(User.name == 'alex').update({}, 字符串)
# session.query(Users.id, Users.name).filter(User.name == 'alex').update({}, 计算)
#
# session.query(Users.id, Users.name).filter(Users.name == 'alex').delete()
