#!/usr/bin/env python
# coding=utf-8
def newfoo(arg1,arg2,*nkw,**kw):
    'display regular args and all variable args'
    print 'arg1 is:',arg1
    print 'arg2 is:',arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:',eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s':%s"%(eachKW,kw[eachKW])
newfoo('wolf',3,'projects',freud=90,gamble=96)
