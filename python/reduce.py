#!/usr/bin/env python
# coding=utf-8
def reduce(bin_func,seq,init=None):
    lseq = list(seq)
    if init is None:
        res = lseq.pop(0)
    else:
        res = init
    for item in lseq:
        res = bin_func(res,item)
    return res
