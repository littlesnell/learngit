#!/usr/bin/env python
# coding=utf-8
def counter(strart_at = 0):
    count = strart_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1
count = counter(5)
print count.next()
print count.next()
print count.send(11)
print count.next()
print count.close()
print count.next()
