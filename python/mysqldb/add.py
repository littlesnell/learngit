#!/usr/bin/env python
# coding=utf-8
from connect import cursor
from connect import conn
import input
class add(object):
    def __init__(self,id,name,age,classes):#定义构造器
        self.id = id
        self.name = name
        self.age = age
        self.classes = classes
    def add_set(self,id,name,age,classes):#定义方法
        self.id = input.id
        self.name = input.name
        self.age = input.age
        self.classes = input.classes
        cursor.execute('INSERT INTO little(id,name,age,class) values (%s,%s,%s,%s)',[input.id,input.name,input.age,input.classes])
conn.commit()

