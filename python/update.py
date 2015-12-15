#!/usr/bin/env python
# coding=utf-8
from connect import cursor
from connect import conn
cursor.execute('select * from little')
values = cursor.fetchall()
for i in range(cursor.rowcount):
    print values[i-1][0],values[i-1][1],values[i-1][2],values[i-1][3]
id = raw_input('请输入你要修改学生的ID:')
print '类别为: id,name,age,class'
subject = raw_input('请输入你要修改学生的类别:')
id1 =raw_input ('请输入修改的%s为:'%subject)
if subject == 'name':
    cursor.execute('update little set name = %s WHERE id = %s',[id1,id])
if subject == 'id':
    cursor.execute('update little set id = %s WHERE id = %s',[id1,id])
if subject == 'age':
    cursor.execute('update little set age = %s WHERE id = %s',[id1,id])
if subject == 'class':
    cursor.execute('update little set class = %s WHERE id = %s',[id1,id])
conn.commit()
