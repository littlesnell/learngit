#!/usr/bin/env python
# coding=utf-8
import functools
def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: ' + text
                func(*args, **kw)
                print 'end call: ' + text
            return wrapper
        return decorator

@log
def  now1():
    print 'doing1...'

@log('text')
def now2():
    print 'doing2...'
