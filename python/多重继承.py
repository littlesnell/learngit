#!/usr/bin/env python
# coding=utf-8
class Animal(object):
    pass
#大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print "running..."
class flyable(object):
    def fly(self):
        print "flying..."
#各种动物
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Runnable):
    pass
class Parrot(Bird,flyable):
    pass
class Ostrich(Bird,flyable):
    pass
