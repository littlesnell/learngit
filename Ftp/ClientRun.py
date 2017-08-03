#!/usr/bin/env python
# coding=utf-8

from FtpClient import Upload_Download_Client
from MacroDefinitionClient import ADDR,BUFSIZ
from socket import *
from time import sleep
import sys
import datetime
import os


def main():
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
        connectinformationserver = tcpCliSock.recv(BUFSIZ)
    except:
        print('连接错误!')
        exit(0)
    if (connectinformationserver == '连接成功'):
    #print connectinformationserver
        while True:
            ChooseUploadDownload(tcpCliSock)
        tcpCliSock.close()
    else:
        print '连接失败，请稍后重试'
        exit(0)



def ChooseUploadDownload(tcpCliSock):
    try:
        uploaddownloadprocess = Upload_Download_Client()
        uploaddownloadprocess.tcpconnect(tcpCliSock)
        while True:
            data = raw_input('请选择上传文件(upload)或下载文件(download):')
            if (data != '上传' and data != 'upload' and data != '下载' and data != 'download'):
                print('输入错误!')
            else:
                tcpCliSock.send(data)
                print data
                break


        if (data == '上传' or data == 'upload'):
            while True:
                filepath = raw_input('请选择上传文件的路径:')
                try:
                    f = open(filepath,'r')
                    tcpCliSock.send(filepath)
                    break
                except:
                    print('该文件不存在，请重新输入!')

            len_filepath = len(filepath)
            while True:
                if filepath[len_filepath-1:len_filepath] != '/':
                    len_filepath = len_filepath - 1
                else:
                    filepath_client = filepath[len_filepath:len(filepath)]
                    break
            print filepath_client
            systemreceive = os.system('ssh ubuntu@123.206.59.16 touch /home/ubuntu/download/%s'%filepath_client)
            if systemreceive != 0:
                print '连接服务器失败!'
                tcpCliSock.send('exit')
                exit(0)
            else:
                try:
                    tcpCliSock.send('successfully')
                    f = open(filepath,'r')
                    start_time = datetime.datetime.now()
                except:
                    print '打开文件错误!'
                    tcpCliSock.send('exit')
                    tcpCliSock.close()
                    exit(0)

            while True:
                print 1


        if (data == '下载' or data == 'download'):
	    systemreceive = os.system('ssh ubuntu@127.0.0.1 ls /home/ubuntu/download  > 1.txt')
            if systemreceive != 0:
                print '连接服务器失败!'
                tcpCliSock.send('exit')
                exit(0)
            while True:
                uploaddownloadprocess.downloadfilelist()
                filename = raw_input('请输入下载的文件名:')
                return_find = uploaddownloadprocess.downloadfileprocess(filename,tcpCliSock)
                if return_find == 'find_successful':
                    break

            while True:
                filepath = raw_input('请选择保存文件的路径:')#客户端自己确认保存位置
                filepath = filepath + '/' +filename
                try:
                    f = open(filepath,'w')
                    f.close()
                    break
                except:
                    print '该路径不存在!'


            if data == 'exit' or not data:
            	tcpCliSock.send('exit')
           	tcpCliSock.close()
            	exit(0)
            else:
            	sleep(0.5)
            	tcpCliSock.send('ok')
            	exitdata = tcpCliSock.recv(BUFSIZ)
            	tcpCliSock.send('lens')
            	filelen = tcpCliSock.recv(BUFSIZ)
            	all_sum = int(filelen)

            	if exitdata == 'ok received successfully':
                    filelencount = 0
                    last_filelencount = 0
                    try:
                        f = open(filepath,'w')
                        start_time = datetime.datetime.now()
                    except:
                    	print '打开文件错误!'
                    	tcpCliSock.send('exit')
                    	tcpCliSock.close()
                    	exit(0)
		    i = 0
                    while True:
		    	try:
			    i = 0
			    sendlength = tcpCliSock.recv(BUFSIZ)
			    tcpCliSock.send('receive sendlength')
			    #print 'sendlength',sendlength
			    while str(i) != sendlength:
                    		filedata = tcpCliSock.recv(BUFSIZ)
				f.write(filedata)
				i += len(filedata)
                    		filelencount += len(filedata)
                        	returnvalue = DownloadSpeed(all_sum,start_time,last_filelencount,filelencount)
				if returnvalue == 'ok':
                            	    last_filelencount = filelencount
                            	    start_time += datetime.timedelta(seconds=1)
				    #print len(filedata)
				    #print '\n\n\n\n\n'
                    		    #f.write(filedata)
			    if filedata != 0:
                    	        tcpCliSock.send('receive successfully! ')
			    	#i = i + 1
			    	#print i
			    else:
			    	print ('异常传输!')
			    	tcpCliSock.send('exit')
			    	tcpCliSock.close()
			    	exit(0)

                    	    #if returnvalue == 'ok':
			    #    last_filelencount = filelencount
			    #    start_time += datetime.timedelta(seconds=1)

                    	    if str(filelencount) == filelen:
			    	all_sum = int(all_sum/1024.0)
			    	sys.stdout.write(str(100) + '%[' + str(all_sum) + 'KB/' + str(all_sum) + 'KB]                    ' + str(0) + 'KB/s     ' + str(0) + 'min' + str(0) + 'sec' + '\r')
                            	returnvalue = DownloadSpeed(all_sum,start_time,last_filelencount,filelencount)
			    	#print '\n传输完成'
                            	filereceiveresult = tcpCliSock.recv(BUFSIZ)
			    	print '\n' + filereceiveresult
                            	f.close()
			    	break
			    	#exit(0)

		        except KeyboardInterrupt:
                            print('\r异常退出')
                            tcpCliSock.send('exit')
			    tcpCliSock.close()
			    exit(0)


    except KeyboardInterrupt:
        print('\r异常退出')
        tcpCliSock.send('exit')
        tcpCliSock.close()
        exit(0)


def DownloadSpeed(all_sum,start_time,last_filelencount,filelencount):
    running_time = datetime.datetime.now()
    if (running_time-start_time).seconds == 1:
	#print start_time
	#print 'change'
	#print running_time
    	speed = int(filelencount/(all_sum*1.0)*100)
        now_filelencount = (filelencount-last_filelencount)/1024.0
	filelencount = int(filelencount/1024.0)
	all_sum = int(all_sum/1024.0)
	need_time = int((all_sum-filelencount)/now_filelencount)
        need_minutes = 0
	need_seconds = 0
	if need_time >= 0 and need_time < 60:
	    need_seconds = need_time
	if need_time >= 60:
	    need_minutes = int(need_time/60.0)
	    need_seconds = need_time-need_minutes*60
	now_filelencount = str(now_filelencount)
	sys.stdout.write(str(speed) + '%[' + str(filelencount) + 'KB/' + str(all_sum) + 'KB]                    ' + now_filelencount[0:5] + 'KB/s     ' + str(need_minutes) + 'min' + str(need_seconds) + 'sec' + '\r')
	sys.stdout.flush()
	return 'ok'




if __name__ == '__main__':
    main()
