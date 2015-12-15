#!/usr/bin/env python
# coding=utf-8

class HotelRoomCalc(object):
    'Hotel room rate calculator'
    def __init__(self,rt,sales = 0.085,rm = 0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate =rt

    def calctotal(self,days = 1):
        'Calculate total;default to daily rate'
        daily = round((self.roomRate*(1 + self.salesTax + self.roomTax)),2)
        return float(days)*daily

s = HotelRoomCalc(299)
s.calctotal()
