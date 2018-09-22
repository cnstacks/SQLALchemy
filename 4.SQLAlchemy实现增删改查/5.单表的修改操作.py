#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 15:38
# File    : 5.单表的修改操作.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import models

engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
maker = sessionmaker(engine)

session = maker()

# 更新操作；˚
session.query(models.Classes).filter(models.Classes.id > 0).update({models.Classes.name: models.Classes.name + "999"},
                                                                   synchronize_session=False)
session.commit()
session.close()
