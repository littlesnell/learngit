#!/usr/bin/env python
# coding=utf-8

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor %d is %d' % (num,count)
            break
        count -= 1
    else:
        print num,'is prime'
for eachNum in range(10,21):
    showMaxFactor(eachNum)
