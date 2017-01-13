s = 'caxlsddmcm'

count = 0
start = 0
end = 0
temp = 0

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        count += 1
    else:
       if temp == 0 and count != 0:
           temp = count
           end = i
           start = end - count
           count = 0
       elif temp < count:
           temp = count
           end = i
           start = end - count
           count = 0 
       elif temp >= count:
           count = 0
           
if count > temp:
    end = i + 1
    start = end - count
           
print('Longest substring in alphabetical order is:',s[start:end+1])
 
           
           
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:08:22 2017

@author: mahmoodserry
"""

