#!/usr/bin/env python
# coding=utf-8
#导入mysql驱动
import MySQLdb

import connect1
#进行连接数据库
conn = MySQLdb.connect(host = connect1.host,user = connect1.user,passwd = connect1.passwd,db = connect1.db,port =connect1.port,charset = 'utf8')
cursor = conn.cursor()
