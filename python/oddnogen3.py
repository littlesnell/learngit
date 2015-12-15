#!/usr/bin/env python
# coding=utf-8

from random import randint as ri
print [n for n in [ri(1,99) for i in range(9)] if n%2]
