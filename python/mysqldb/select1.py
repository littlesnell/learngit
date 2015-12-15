#!/usr/bin/env python
# coding=utf-8
from connect import cursor
print "请选择查询的方式"
print "1-按ID查询"
print "2-按姓名查询"
print "3-按年龄查询"    
print "4-按班级查询"
b = input( "请输入你的选择:")
if b==1:
    id = raw_input('请输入你要查询的ID:')
    cursor.execute('select * from little where id = %s',id)
    values = cursor.fetchone()
    print values[0],values[1],values[2],values[3]
if b==2:
    name = raw_input('请输入你要查询的姓名:') 
    cursor.execute('select * from little where name = %s',name)
    values = cursor.fetchall()
    for i in range(cursor.rowcount):
        print values[i-1][0],values[i-1][1],values[i-1][2],values[i-1][3]
if b==3:
    age = raw_input('请输入你要查询的年龄:')
    cursor.execute('select * from little where age = %s',age)
    values = cursor.fetchall()
    for i in range(cursor.rowcount):
        print values[i-1][0],values[i-1][1],values[i-1][2],values[i-1][3]
if b==4:
    classes = raw_input('请输入你要查询的班级:')
    cursor.execute('select * from little where class = %s',classes)
    values = cursor.fetchall()
    for i in range(cursor.rowcount):
        print values[i-1][0],values[i-1][1],values[i-1][2],values[i-1][3]
