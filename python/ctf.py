#!/usr/bin/env python
# coding=utf-8
def countToFour1():
    for eachNum in range(5):
        print eachNum,
def countToFour2(n):
    for eachNum in range(n,5):
        print eachNum,
def countToFour3(n=1):
    for eachNum in range(n,5):
        print eachNum,
print countToFour3(2)
print countToFour3(4)
print countToFour3(5)
