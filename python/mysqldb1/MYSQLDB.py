#!/usr/bin/env python
# coding=utf-8
#导入mysql驱动
import MySQLdb

import add
import delete
import update
import select1

host = 'localhost'
user = 'root'
passwd = '111111'
db = 'littledog'
port = 3306
charset = 'utf8'
#tablename = 'little'
#进行连接数据库
conn = MySQLdb.connect(host = host,user = user,passwd = passwd,db = db,port = port,charset = charset)
cursor = conn.cursor()

a = 0
while a!=5:
    print "1-查询数据"
    print "2-修改数据"
    print "3-删除数据"
    print "4-增添数据"
    print "5-退出"
    a = input("请输入你的选择:")
    
    if a==5:
        exit
    #应填入依次为id，name，age，class
    if a==4:
        add.add('53','py','20','c++学习班',cursor,conn)
    #应填入依次为id，name（依照选择删除的方式id/name）
    if a==3:
        delete.delete('53','py',cursor,conn)
    #应填入依次为id，修改的信息，修改信息的类别
    if a==2:
        update.update('52','python学习班','class',cursor,conn)
    #应填入依次为id，name，age，class（依照选择查询的方式id/name/age/class）
    if a==1:
        select1.select('1','py','20','c++学习班',cursor,conn)
cursor.close()
conn.close()
