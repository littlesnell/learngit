#!/usr/bin/env python
# coding=utf-8

from FtpServer import Upload_Download_Server
from socket import *
from MacroDefinitionServer import ADDR,BUFSIZ
from time import ctime
import threading
import datetime




def main():
    #ss.connect()
    tcpSerSock = socket(AF_INET,SOCK_STREAM)# 创建一个套接字
    #ss.bind()
    try:
        tcpSerSock.bind(ADDR)# 绑定主机号，IP到套接字
    except:
        print '端口被占用，请稍后重试!'
        exit(0)
    #ss.listen()
    tcpSerSock.listen(5)# 监听数量最多为5
        
    while True:  
        #服务器套接字通过socket的accept方法等待客户请求一个连接
        try:
            print 'waiting for connection...\n'
            tcpCliSock,addr = tcpSerSock.accept()
            a = datetime.datetime.now()
            t = threading.Thread(target=tcplink_server, args=(tcpCliSock,addr,a))
            t.start()
            print '...connected from:',addr
            print 'start at:',ctime()
        except KeyboardInterrupt:
            print '\r服务器端程序结束'
            exit(0)
    tcpSerSock.close()
    


def tcplink_server(tcpCliSock,addr,a):
    tcpCliSock.send('连接成功')#失败没考虑
    while True:
        ChooseUploadDownload(tcpCliSock,a,addr)
    tcpCliSock.close()

def ChooseUploadDownload(tcpCliSock,a,addr):
    try:
        uploadanddownloadprocessserver = Upload_Download_Server()
        choose_upload_or_download =  tcpCliSock.recv(BUFSIZ)
        if choose_upload_or_download == 'exit':
            b = datetime.datetime.now()
            print '...connected from:',addr
            print 'end at:',ctime()
            print 'running time: %s seconds'%(b-a).seconds
            print 'waiting for connection...\n'
            exit(0)
            tcpCliSock.close()


        print 'choose_upload_or_download',choose_upload_or_download
        if choose_upload_or_download == 'download' or choose_upload_or_download == '下载':
            uploadanddownloadprocessserver.downloadfileprocess(tcpCliSock,a,addr)
        if choose_upload_or_download == 'upload' or choose_upload_or_download == '上传':
            print 123
            a = uploadanddownloadprocessserver.uploadfileprocess(tcpCliSock,a,addr)
            print 456
    except:
        exit(0)
    #print data
    #if data == 'exit':
    #    b = datetime.datetime.now()
    #    print '...connected from:',addr
    #    print 'end at:',ctime()
    #    print 'running time: %s seconds'%(b-a).seconds
    #    print 'waiting for connection...'
    #    exit(0)


if __name__ == '__main__':
    main()

#uploadprogram = Upload_Download_Server()    #上传和下载实例化
#uploadprogram.uploadfile()

