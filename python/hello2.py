#!/usr/bin/env python
# coding=utf-8
a=raw_input('name=')
b=int(raw_input('score='))
class Student(object):
    def __init__ (self,name,score):
        self.name=name
        self.score=score
    def get_grade(self,n):
        if n==1:
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'
        if n==2:
            if self.score >= 90:
                return 'A'
            elif self.score>=80:
                return 'B'
            else:
                return 'C'

join = Student(a,b)
c=input('请输入选择的评判标准(1~2)：')
print join.get_grade(c);




