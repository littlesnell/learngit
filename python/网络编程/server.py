#!/usr/bin/env python
# coding=utf-8

from hong import host,port
import socket
import Queue
import select
import traceback
import time

class SelectServer():
    def __init__(self):
        self.dict_name = {}#客户端
        self.dict_msg = {}#消息队列
        self.listen_fd = 0#初始化监听的文件描述符
        self.inputs = []#可读状态
        self.outputs = []#可写状态
    def run(self):
        '''用select监听socket'''
        s = socket.socket()#默认ip，tcp协议
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#地址复用
        s.bind(host,port)
        s.listen(5)
