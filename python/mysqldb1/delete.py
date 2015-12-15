#!/usr/bin/env python
# coding=utf-8
def delete(id,name,cursor,conn):
    print "请选择删除信息的类别"
    print "1-按ID删除"
    print "2-按NAME删除"
    c = input("请输入你的选择:")
    if c==1:
        cursor.execute('DELETE FROM little WHERE id = %s',id)
    if c==2:
        cursor.execute('DELETE FROM little WHERE name = %s',name)
    conn.commit()
