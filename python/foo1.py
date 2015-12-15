#!/usr/bin/env python
# coding=utf-8
def foo():
    def bar():
        print 'bar() called'
    print 'foo() called'
    bar()
foo()
#bar()没有定义
