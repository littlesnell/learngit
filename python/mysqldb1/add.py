#!/usr/bin/env python
# coding=utf-8
def add(id,name,age,classes,cursor,conn):
    if( cursor.execute('INSERT INTO little (id,name,age,class) values (%s,%s,%s,%s)',[id,name,age,classes])):
        print("插入成功！")
    else:
        print("插入失败！")
    conn.commit()

