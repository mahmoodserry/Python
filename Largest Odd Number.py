x, y, z, temp = 50003, 5001, 0.1, 0

if x%2 != 0:
    temp = x
    if y%2 != 0 and y > temp:
        temp = y
    elif z%2 != 0 and z > temp:
        temp = z
else:
    if y%2 != 0:
        temp = y
        if z%2 != 0 and z > temp:
            temp = z
    elif z%2 != 0:
        temp = z


if temp == 0:
    print('No odd Numbers!')
else:
    print('Largest Odd Number is:',temp)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:49:16 2017

@author: mahmoodserry
"""

