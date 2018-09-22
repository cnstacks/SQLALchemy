#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: SQLALchemy 
# Software: PyCharm
# Time    : 2018-09-22 11:14
# File    : 1.创建表操作.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index, DateTime, ForeignKey
from sqlalchemy import create_engine
import datetime

Base = declarative_base()


# 创建表;
class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, unique=True)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=True, index=True)
    password = Column(String(64), nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)  # 不能这么写datatime.datetime.now，
    class_id = Column(Integer, ForeignKey('classes.id'))


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


# SQLAlchemy不会自动创建第三表;
class Student2Hobby(Base):
    __tablename__ = 'student2hobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student_id'))
    hobby_id = Column(Integer, ForeignKey('hobby_id'))
    # 创建联合唯一索引;
    UniqueConstraint('student_id', 'hobby_id', name='uix_student_id_hobby_id')
    # Index('ix_id_name','name','extra')


def init_db():
    # 数据库连接相关；
    engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
    # 创建表；
    Base.metadata.create_all(engine)


def drop_db():
    # 数据库连接相关；
    engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/flask_session?charset=utf8")
    # 删除表;
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    init_db()
    # drop_db()
