#!/usr/bin/env python
#encoding=utf-8
# 导入MySQL驱动
import MySQLdb
#进行连接数据库
conn = MySQLdb.connect(host="localhost",user="root",passwd="111111",db="littledog",port=3306,charset="utf8")
cursor = conn.cursor()
# 创建用户表
#cursor.execute('create table ceshi (id varchar(20) primary key, name varchar(20),age int,class varchar(50))')
# 菜单选择
a = 1#防止while无法正常运行
while a!=5:
    print "1-查询数据"
    print "2-修改数据"
    print "3-删除数据"
    print "4-增添数据"
    print "5-退出"
    a = input("请输入你的选择:")
    if a==1:#有问题
        # 运行查询:
        print "请选择查询的方式"
        print "1-按ID查询"
        print "2-按姓名查询"
        print "3-按年龄查询"    
        print "4-按班级查询"
        b =input( "请输入你的选择")
        if b==1:
            id = raw_input('请输入你要查询的ID:')
            cursor.execute('select * from ceshi where id = %s',id)
            values = cursor.fetchall()
            print values
        if b==2:
            name = raw_input('请输入你要查询的姓名')
            cursor.execute('select * from ceshi where name = %s',name)
        if b==3:
            age = raw_input('请输入你要查询的年龄')
            cursor.execute('select * from ceshi where age = %s',age)
        if b==4:
            classes = raw_input('请输入你要查询的班级')
            cursor.execute('select * from ceshi where class = %s',classes)
        cursor = conn.cursor()
        cursor.execute('select * from ceshi where id = %s','1' )
        values = cursor.fetchall()



    #if a==2:
    if a==3:
        # 删除数据
        id = raw_input('请输入你要删除数据的ID:')
        cursor.execute('delete * from ceshi where id = %s',id)
    if a==4:
        # 插入数据
        id = raw_input('id:')
        name = raw_input('name:')
        age = raw_input('age:')
        classes = raw_input('class:')
        cursor.execute('insert into ceshi (id,name,age,class) values (%s,%s,%s,%s)',[id,name,age,classes])
        #提交事物
        conn.commit()
    if a==5:   
        exit


