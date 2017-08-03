#!/usr/bin/env python
# coding=utf-8

import os
from socket import *
from MacroDefinitionClient import BUFSIZ





class Upload_Download_Client(object):
    
    def __init__(self,upload=0,download=0):
        self.upload = upload
        self.download = download

    def tcpconnect(self,tcpCliSock):
        self.tcpCliSock = tcpCliSock

    def uploadfile(self,pwd):
        self.pwd = pwd

    def uploadfileprocess(self,filepath,tcpCliSock):
        return 1
    def downloadfile(self,pwd):
        self.pwd = pwd


    def downloadfilelist(self):#显示文件列表
        print '\n以下为文件列表:'
        f = open('1.txt')
        for line in f.readlines():
            print (line.strip())
        print '\n'
        f.close()

    def downloadfileprocess(self,filename,tcpCliSock):#下载文件
        i = 0
        f = open('1.txt')
        for line in f.readlines():
            if filename == line[0:len(line)-1]:
                i = 1
                break
        f.close()
        if i == 1:
            #print'发送'
            tcpCliSock.send(filename)
            filename_reply = tcpCliSock.recv(BUFSIZ)
            #print filename_reply
            return 'find_successful'


        if i == 0:
            print '没有该文件,请重新选择!'

