#!/usr/bin/env python
# coding=utf-8

s = 'abcde'
for i in [None] + range(-1,-len(s),-1):
    print s[:i]
