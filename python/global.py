#!/usr/bin/env python
# coding=utf-8

is_this_global = 'xyz'
def foo():
    global is_this_global
    this_is_local = 'abc'
    is_this_global = 'def'
    print this_is_local + is_this_global


foo()
print is_this_global
