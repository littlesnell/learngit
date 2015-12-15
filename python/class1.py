#!/usr/bin/env python
# coding=utf-8
    
class TestStaticMethod:
    def foo():
        print 'calling static method foo()'
        
    foo = staticmethod(foo)

class TestStaticMethod:
    @staticmethod
    def foo():
        print 'calling static method foo()'

tsm = TestStaticMethod()
tsm.foo()
TestStaticMethod.foo()



