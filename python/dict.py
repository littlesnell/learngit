#!/usr/bin/env python
# coding=utf-8

def dictVarArgs(arg1,arg2='defaultB',**theRest):
    'display 2 regular args and keyword variable args'
    print 'formal arg1:',arg1
    print 'formal arg2:',arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s:%s'%(eachXtrArg,str(theRest[eachXtrArg]))


dictVarArgs(1220,740.0,c='grail')
print '\n'
dictVarArgs(arg2='tales',c=123,d='poe',arg1='mystery')
print '\n'
dictVarArgs('one',d=10,e='zoo',men=('freud','gaudi'))
