#!/usr/bin/env python
# coding=utf-8
a=raw_input('name:')
b=input('score:')
class Student(object):
    def __init__ (self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print '%s : %s' %(self.__name,self.__score)
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
c = Student(a,b)
c.print_score()
print c.get_name()
print c.get_score()
d = input('请输入修改后的成绩:')
c.set_score(d)
print c.get_score()

