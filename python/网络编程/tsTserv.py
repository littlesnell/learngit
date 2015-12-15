#!/usr/bin/env python
# coding=utf-8

import MySQLdb
import threading
from socket import *
from time import ctime
from hong import PORT
from hong import BUFSIZ
from hong import ADDR

#ss = socket()
HOST = ''
PORT
def main():
    tcpSerSock = socket(AF_INET,SOCK_STREAM)# 创建一个套接字

    #ss.bind()
    tcpSerSock.bind(ADDR)# 绑定主机号，IP到套接字

    #ss.listen()
    tcpSerSock.listen(5)# 监听数量最多为5
    
    while True:  
        #服务器套接字通过socket的accept方法等待客户请求一个连接
        try:
            print 'waiting for connection...'
            tcpCliSock,addr = tcpSerSock.accept()
            t = threading.Thread(target=tcplink_server, args=(tcpCliSock, addr))
            t.start()
            print '...connected from:',addr
            print 'start at:',ctime()
        except KeyboardInterrupt:
            print '程序结束'
            exit(0)
    tcpSerSock.close()

def tcplink_server(tcpCliSock, addr):
    while True:
        a = tcpCliSock.recv(BUFSIZ)
        if a[8:] == '2' and a[0:8] == 'chooce1:':
            tcpCliSock.send('正常退出!')
            tcpCliSock.close()
            break
        else:
            if a[0:8] == 'chooce1:':
                tcpCliSock.send('接收成功!')
                a = a[8:]
                if a == '0':
                    regidter_server(tcpCliSock)
                if a == '1':
                    log_in_server(tcpCliSock)
            else:
                tcpCliSock.send('接收失败!')
                tcpCliSock.close()
                exit(0)


        #if data == 'exit' or not data:
         #   break
    tcpCliSock.close()
    print 'Connection from %s:%s closed.' % addr
    print 'waiting for connection...'


def regidter_server(tcpCliSock):
    b = tcpCliSock.recv(BUFSIZ)
    if b[0:8] =='chooce2:':
        tcpCliSock.send('接收成功!')
        b = b[8:]
        if b == '0':
            student_regidter_server(tcpCliSock)
        if b == '1':
            teacher_regidter_server(tcpCliSock)
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)

def log_in_server(tcpCliSock):
    c = tcpCliSock.recv(BUFSIZ)
    if c[0:8] == 'chooce3:':
        tcpCliSock.send('接收成功!')
        print c
        c = c[8:]
        print c
        if c == '0':
            student_log_in_server(tcpCliSock)
        if c == '1':
            teacher_log_in_server(tcpCliSock)
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)

def student_log_in_server(tcpCliSock):
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    name_server = tcpCliSock.recv(BUFSIZ)
    print name_server
    print 'name_server =%s'%name_server[0:12]
    if name_server[0:12] == 'name_client:':
        tcpCliSock.send('接收成功!')
        print name_server
        name_server = name_server[12:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    passwd_server = tcpCliSock.recv(BUFSIZ)
    print passwd_server[0:14]
    if passwd_server[0:14] == 'passwd_client:':
        tcpCliSock.send('接收成功!')
        print passwd_server
        passwd_server = passwd_server[14:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    if (cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s',[name_server,passwd_server])):
        tcpCliSock.send('登陆成功!')
        menu_student_server(tcpCliSock)
    else:
        tcpCliSock.send('登陆失败!')
        tcpCliSock.close()
        exit(0)



def teacher_log_in_server(tcpCliSock):
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    name_server = tcpCliSock.recv(BUFSIZ)
    print name_server
    print 'name_server =%s'%name_server[0:12]
    if name_server[0:12] == 'name_client:':
        tcpCliSock.send('接收成功!')
        print name_server
        name_server = name_server[12:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    passwd_server = tcpCliSock.recv(BUFSIZ)
    print passwd_server[0:14]
    if passwd_server[0:14] == 'passwd_client:':
        tcpCliSock.send('接收成功!')
        print passwd_server
        passwd_server = passwd_server[14:]
    else:
        tcpCliSock.send('接收失败!')
        tcpCliSock.close()
        exit(0)
    if (cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s',[name_server,passwd_server])):
        tcpCliSock.send('登陆成功!')
        menu_teacher_server(tcpCliSock)
    else:
        tcpCliSock.send('登陆失败!')
        tcpCliSock.close()
        exit(0)





def student_regidter_server(tcpCliSock):
    name = tcpCliSock.recv(BUFSIZ)
    #print name[5:]
    if name[0:5] == 'name:':
        tcpCliSock.send('用户名接收成功!')
        name = name[5:]
        #print 'name = %s'%name
        passwd =tcpCliSock.recv(BUFSIZ)
        if passwd[0:7] == 'passwd:':
            tcpCliSock.send('密码接收成功!')
            passwd = passwd[7:]
         #   print 'passwd = %s'%passwd
            student_connect_server(name,passwd,tcpCliSock)
        else:
            tcpCliSock.send('密码接收失败!')
            tcpSerSock.close()
            exit(0)
    else:
        tcpCliSock.send('用户名接收失败!')
        tcpSerSock.close()
        exit(0)


def teacher_regidter_server(tcpCliSock):
    name = tcpCliSock.recv(BUFSIZ)
    #print name[5:]
    if name[0:5] == 'name:':
        tcpCliSock.send('用户名接收成功!')
        name = name[5:]
        #print 'name = %s'%name

        passwd =tcpCliSock.recv(BUFSIZ)
        if passwd[0:7] == 'passwd:':
            tcpCliSock.send('密码接收成功!')
            passwd = passwd[7:]
            #print 'passwd = %s'%passwd

            command = tcpCliSock.recv(BUFSIZ)
            #print command
            #print command[0:8]
            #print command[8:]
            if command[0:8] == 'command:' and command[8:] == 'teacher':
                tcpCliSock.send('口令接收成功!')
                teacher_connect_server(name,passwd,tcpCliSock)
            else:
                tcpCliSock.send('口令接收错误!')
                tcpCliSock.close()
                exit(0)

        else:
            tcpCliSock.send('密码接收失败!')
            tcpSerSock.close()
            exit(0)

    else:
        tcpCliSock.send('用户名接收失败!')
        tcpSerSock.close()
        exit(0)



def student_connect_server(name,passwd,tcpCliSock):#学生连接
    passwd1 = passwd
    #print 'passwd1 = %s'%passwd1
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306,charset = 'utf8')
    cursor = conn.cursor()
    student_write_server(name,passwd1,conn,cursor,tcpCliSock)






def teacher_connect_server(name,passwd1,tcpCliSock):#教师连接
    conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
    cursor = conn.cursor()
    teacher_write_server(name,passwd1,conn,cursor,tcpCliSock)






def teacher_write_server(name,passwd1,conn,cursor,tcpCliSock):#教师注册
    if (cursor.execute('INSERT INTO user1 (name,password)VALUES (%s,%s)',[name,passwd1])):
        tcpCliSock.send('注册成功!')
    else:
        tcpCliSock.send('注册失败!')
    conn.commit()
    conn.close()




def student_write_server(name,passwd1,conn,cursor,tcpCliSock):#学生注册
    if (cursor.execute('INSERT INTO user (name,password) VALUES (%s,%s)',[name,passwd1])):
        tcpCliSock.send('注册成功!')
    else:
        tcpCliSock.send('注册失败!')
    conn.commit()
    conn.close()

def menu_student_server(tcpCliSock):
    d = tcpCliSock.recv(BUFSIZ)
    print d
    if d[2:] == '2' and d[0:2] == 'd:':
        tcpCliSock.send('正常退出!')
        tcpCliSock.close()
        exit(0)
    else:
        if d[0:2] == 'd:':
            tcpCliSock.send('发送成功!')
            d = d[2:]
            print d
            if d == '1':
               score_select_server(tcpCliSock)
        else:
            tcpCliSock.send('发送失败!')
            tcpCliSock.close()
            exit(0)
     

def score_select_server(tcpCliSock):
    e = tcpCliSock.recv(BUFSIZ)
    print e
    if e[0:2] == 'e:':
        tcpCliSock.send('接收成功!')
        e = e[2:]
        print e
        conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '111111',db = 'password',port = 3306 ,charset = 'utf8')
        cursor = conn.cursor()
        if e == '1':
            print '按学号查询'
            number = tcpCliSock.recv(BUFSIZ)
            print 'number = %s'%number
            if number[0:7] == 'number:':
                tcpCliSock.send('number接收成功!')
                number = number[7:]
            else:
                tcpCliSock.send('number接收失败!')
                tcpCliSock.close()
                exit(0)
            if (cursor.execute('SELECT * FROM  score WHERE number = %s'%number)):
                tcpCliSock.send('查询成功!')
                values = cursor.fetchone()
                print type(values[0])
                s = values[0].encode("utf-8")
                tcpCliSock.send(s)
            else:
                tcpCliSock.send('查询失败!')
                tcpCliSock.close()
                exit(0)
    else:
        tcpCliSock.send('发送失败!')
        tcpCliSock.close()
        exit(0)




def menu_teacher_server(tcpCliSock):
    print 'menu_teacher_server'


if __name__ == '__main__':
    main()
