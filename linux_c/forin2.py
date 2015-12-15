#!/usr/bin/env python
# coding=utf-8
year = int(raw_input("请输入年份："))
if(year>=2000):
    print '00后'
elif(year>=1990):
    print '90后'
else:
    print '待定'
