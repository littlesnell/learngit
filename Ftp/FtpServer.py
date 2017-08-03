#!/usr/bin/env python
# coding=utf-8

import datetime
from socket import *
from MacroDefinitionServer import BUFSIZ
from time import ctime,sleep


#上传，下载
class Upload_Download_Server(object):     
    def __init__(self,upload=0,download=0): #默认不进行操作
        self.upload = upload
        self.download = download

    def uploadfile(self,pwd):
        self.pwd = pwd
        print 1

    def downloadfile(self,pwd):
        self.pwd = pwd

    def uploadfilelist(self):
        return 1

    def uploadfileprocess(self,tcpCliSock,a,addr):
        filepath = tcpCliSock.recv(BUFSIZ)
        if filepath == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()
        systemreceive = tcpCliSock.recv(BUFSIZ)
        if systemreceive == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()

        while Ture:
            print 1


        print 'systemreceive',systemreceive

        print filepath
    
    def downloadfilelist(self):
        return 1

    def downloadfileprocess(self,tcpCliSock,a,addr):
        filename = tcpCliSock.recv(BUFSIZ)
        print filename
	filename = '/home/ubuntu/download/' + filename
        if filename[22:len(filename)] == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()



        tcpCliSock.send('document received successfully')
        exit_or_len = tcpCliSock.recv(BUFSIZ)
        #print exit_or_len
        tcpCliSock.send(exit_or_len + ' received successfully')
        if  exit_or_len == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()
        filelen = 0#文件总大小

        #节省换行
        if filename[22:len(filename)] == 'exit' or exit_or_len == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()
        else:
            file_lens = Upload_Download_Server()
            filelen = file_lens.data_len(addr,filelen,filename)
            filelen = str(filelen)
            lens = tcpCliSock.recv(BUFSIZ)
            tcpCliSock.send(filelen)

            f = open(filename)
            while True:
                data = f.read(BUFSIZ)
		if len(data) == 0:
		    tcpCliSock.send('传输完成!')
		    break
		    #b = datetime.datetime.now()
		    #print 'cccccccc'
                    #print '...connected from:',addr
                    #print 'end at:',ctime()
                    #print 'running time: %s seconds'%(b-a).seconds
                    #print 'waiting for connection...\n'
                    #exit(0)
                    #tcpCliSock.close()
		#print 'len(data)',len(data)
		lengthdata = str(len(data))
		tcpCliSock.send(lengthdata)
		sendlength = tcpCliSock.recv(BUFSIZ)
		#print 'sendlength',sendlength
		tcpCliSock.send(data)
                data_receive = tcpCliSock.recv(BUFSIZ)
		#print data_receive + '\n'
                if data_receive == 'exit':
                    b = datetime.datetime.now()
                    print '...connected from:',addr
                    print 'end at:',ctime()
                    print 'running time: %s seconds'%(b-a).seconds
                    print 'waiting for connection...\n'
                    exit(0)
                    tcpCliSock.close()
                if not data:
                    f.close()



    def data_len(self,addr,filelen,filename):
        print addr,
        print '请求文件为:',filename
        try:
            f = open(filename)
            while True:
                data = f.read(BUFSIZ)
                filelen += len(data)
                if not data:
                    return filelen
                    f.close()
        except:
            print '文件打开异常'
	    tcpCliSock.close()
            exit(0)




