#!/usr/bin/env python
# coding=utf-8
a=input('请输入合理的成绩：')
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score=value
b = Student()
b.set_score(a)
print b.get_score()
c=input('请输入一个非法的成绩:')
b.set_score(c)
d=raw_input('请输入一个非int型的成绩:')
b.set_score(d)
