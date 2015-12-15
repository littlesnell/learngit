#!/usr/bin/env python
# coding=utf-8
def update(id,id1,subject,cursor,conn):
    cursor.execute('select * from little')
    values = cursor.fetchall()
    for i in range(cursor.rowcount):
        print values[i-1][0],values[i-1][1],values[i-1][2],values[i-1][3]
    if subject == 'name':
        cursor.execute('update little set name = %s WHERE id = %s',[id1,id])
    if subject == 'id':
        cursor.execute('update little set id = %s WHERE id = %s',[id1,id])
    if subject == 'age':
        cursor.execute('update little set age = %s WHERE id = %s',[id1,id])
    if subject == 'class':
        cursor.execute('update little set class = %s WHERE id = %s',[id1,id])
    conn.commit()
