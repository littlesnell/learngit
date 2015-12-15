#!/usr/bin/env python
# coding=utf-8


#连接数据库
import connect
a = 0 
while a!=5:
    print "1-查询数据"
    print "2-修改数据"
    print "3-删除数据"
    print "4-增添数据"
    print "5-退出"
    a = input("请输入你的选择:")

    #导入自定义模块
    connect

    #选择导入模块
    if a==1:
        import select1
        select1
    if a==2:
        import update
        update
    if a==3:
        import delete
        delete
    if a==4:
        import add
        add
    if a==5:
        import exit
        exit


    #增添数据
    #add
    #删除数据
    #delete
    #退出
    #exit
    #修改数据
    #update
    #查询数据
    #select
