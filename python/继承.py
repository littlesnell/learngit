#!/usr/bin/env python
# coding=utf-8
class Animal(object):
    def run(self):
        print "Animal is running..."
class Dog(Animal):
    def run(self):
        print "Dog is running..."
    def eat(self):
        print "Eating meat..."
class Cat(Animal):
    def run(self):
        print "Cat is running..."
    def eat(self):
        print "Eating milk..."

dog = Dog()
print 'dog:'
dog.run()
dog.eat()
cat = Cat()
print 'cat:'
cat.run()
cat.eat()

