#!/usr/bin/env python
# coding=utf-8

from random import randint

allNums = []
for eachNum in range(9):
    allNums.append(randint(1,99))
print filter(lambda n: n%2 ,allNums)
