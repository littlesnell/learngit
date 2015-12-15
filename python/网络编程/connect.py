#!/usr/bin/env python
# coding=utf-8
import MySQLdb
name = 'py'
passwd1 ='1234'
def connect(name,passwd1):
    conn = MySQLdb.connect(host = '127.0.0.1',user = 'root',passwd = '111111',db = 'littledog',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    print name
    print passwd1
    print conn
    print cursor
    write(name,passwd1,conn,cursor)

def write(name,passwd1,conn,cursor):
    print name
    print passwd1
    if (cursor.execute('insert into user1 (name,password) values (%s,%s)',[name,passwd1])):
        print '写入成功!'
    else:
        print '写入失败!'
    conn.commit()
if __name__ == '__main__':
    connect(name,passwd1)
