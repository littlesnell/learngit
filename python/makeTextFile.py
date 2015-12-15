#!/usr/bin/env python
# coding=utf-8

'makeTextFile.py -- create text file'


import os
ls = os.linesep

# get filename

while True:

    fname = raw_input('Enter a text name:')
    if os.path.exists(fname):
        print "ERROR:'%s' already exists" % fname
    else:
        break

#get file content (text) lines

all = []
print "\nEnter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('> ')
    if not entry or entry == 'exit':
        break
    else:
        all.append(entry)

#write lines to file with porper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'
