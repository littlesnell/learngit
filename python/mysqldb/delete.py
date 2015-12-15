#!/usr/bin/env python
# coding=utf-8
from connect import cursor
from connect import conn
print "请选择删除信息的类别"
print "1-按ID删除"
print "2-按NAME删除"
c = input("请输入你的选择:")
class delete(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def set_delete(self,id,name):
        if c==1:
            id = raw_input('ID:')
            cursor.execute('DELETE FROM little WHERE id = %s',id)
        if c==2:
            name = raw_input('NAME:')
            cursor.execute('DELETE FROM little WHERE name = %s',name)
conn.commit()
