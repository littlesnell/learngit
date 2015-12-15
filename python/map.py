#!/usr/bin/env python
# coding=utf-8
def map(func,seq):
    mapped_seq = []
    for i in seq:
        mapped_seq.append(func(i))
    return mapped_seq
print map((lambda x:x+2),[0,1,2,3,4,5])
print map(lambda x:x**2,range(6))
print [x+2 for x in range(6)]
print [x**2 for x in range(6)]
