#!/usr/bin/env python
# coding=utf-8

a = input('输入起始值:')
b = input('输入结束值:')
print 'DEC    mZIN    OCT    HEX'
def two(i):
    list = ()
    j = 0
    list[j] = i%2
    i = i/2
    j += 1
    for i 

for i in range(a,b+1):
    print '%d\t'%i,
    print '%o\t'%i,
    print '%X\n'%i,
