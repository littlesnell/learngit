#!/usr/bin/env python
# coding=utf-8

stack = []

def pushit():
    stack.append(raw_input('Enter New string:').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [','stack.pop()',']'

def viewstack():
    print stack

CMDs = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit
Enter choice:"""

while True:
    while True:
        try:
            print 'p(U)sh'
            print 'p(O)p'
            print '(V)iew'
            print '(Q)uit'
            choice = raw_input('Enter choice:').strip()[0].lower()
        except(EOFError,KeyboardInterrupt,IndexError):
            choice = 'q'

        print '\nYou picked:[%s]' % choice
        if choice not in 'uovq':
            print 'Invalid option,try again'
        else:
            break

    if choice == 'q':
        break
    CMDs[choice]()

if __name__ == '__main__':
    showmenu()
