#!/usr/bin/env python
# coding=utf-8
from random import randint
def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0,len(aList)))
for item in randGen(['rock','paper','scissors']):
    print item

