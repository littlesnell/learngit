#!/usr/bin/env python
# coding=utf-8

#import 
from socket import *
from time import ctime
from hong import PORT
from hong import BUFSIZ
from hong import ADDR

#ss = socket()
HOST = ''
PORT
tcpSerSock = socket(AF_INET,SOCK_STREAM)# 创建一个套接字

#ss.bind()
tcpSerSock.bind(ADDR)# 绑定主机号，IP到套接字

#ss.listen()
tcpSerSock.listen(5)# 监听数量最多为5

#inf_loop:
    #cs = ss.accept()
while True:  
    print 'waiting for connection...'
    tcpCliSock,addr = tcpSerSock.accept()
    print '...connected from:',addr
    print 'start at:',ctime()
    
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
        tcpCliSock.send('[%s] %s' %(ctime(),data))

    print 'done at:',ctime()
    tcpCliSock.close()
    #try:
    #    tcpCliSock,addr = tcpSerSock.accept()#可能得到异常的语句
    #except KeyboardInterrupt:#锁定是哪种异常
    #    print 'KeyboardInterrupt error'#出现异常的处理方法
    #    exit(0)
tcpSerSock.close()
