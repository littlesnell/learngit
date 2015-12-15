#!/usr/bin/env python
# coding=utf-8

class p(object):
    def foo(self):
        print 'Hi,I am p-foo()'

class c(p):
    def foo(self):
        print 'Hi,I am c-foo()'

C = c()
C.foo(c)
