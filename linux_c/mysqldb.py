#!/usr/bin/env python
#encoding=utf-8
# 导入MySQL驱动
import MySQLdb
#进行连接数据库
conn = MySQLdb.connect(host="localhost",user="root",passwd="111111",db="littledog",port=3306,charset="utf8")
cursor = conn.cursor()
# 创建用户表
#cursor.execute('create table little (id varchar(20) primary key, name varchar(20),age int,class varchar(50))')
# 菜单选择
a = 1#防止while无法正常运行
while a!=5:
    print "1-查询数据"
    print "2-修改数据"
    print "3-删除数据"
    print "4-增添数据"
    print "5-退出"
    a = input("请输入你的选择:")
    if a==1:
        # 查询数据
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
    if a==2:
        #修改数据
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
    if a==3:
        # 删除数据
        print "请选择删除信息的类别"
        print "1-按ID删除"
        print "2-按姓名删除"
        c = input( "请输入你的选择:" )
        if c==1:
            id = raw_input('请输入你要删除的ID:')
            cursor.execute('delete from little where id = %s',id)
            conn.commit()
        if c==2:
            name = raw_input('请输入你要删除的NAME:')
            cursor.execute('delete from little where name = %s',name)
            conn.commit()
    if a==4:
        # 插入数据
        id = raw_input('id:')
        name = raw_input('name:')
        age = raw_input('age:')
        classes = raw_input('class:')
        cursor.execute('insert into little (id,name,age,class) values (%s,%s,%s,%s)',[id,name,age,classes])
        #提交事物
        conn.commit()
    if a==5:   
        exit
        cursor.close()
        conn.close()


