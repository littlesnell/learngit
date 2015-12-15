#!/usr/bin/env python
# coding=utf-8
def tupleVarArgs(arg1,arg2='deffaultB',*theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg 1:',arg1
    print 'formal arg 2:',arg2
    for eachXtrArg in theRest:
        print 'another arg:',eachXtrArg


tupleVarArgs('abc')
print '\n'
tupleVarArgs(23,4.56)
print '\n'
tupleVarArgs('abc',123,'xyz,456.789')
