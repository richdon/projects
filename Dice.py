# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:05:49 2019

@author: richa
"""

from random import randint
side1 = 0
side2 = 0
side3 = 0
side4 = 0
side5 = 0
side6 = 0

for i in range (0,1000):
    roll = randint(1,6)
    
    if roll == 1:
        side1 += 1
    elif roll == 2:
        side2 +=1
    elif roll == 3:
        side3 +=1
    elif roll == 4:
        side4 +=1
    elif roll == 5:
        side5 += 1
    elif roll == 6:
        side6 +=1
    


print('1' , '#' * side1)
print('2' , '#' * side2)
print('3' , '#' * side3)
print('4' , '#' * side4)
print('5' , '#' * side5)
print('6' , '#' * side6)

print('you have rolled 1' , side1, 'times')
print('you have rolled 2' , side2, 'times')
print('you have rolled 3' , side3, 'times')
print('you have rolled 4' , side4, 'times')
print('you have rolled 5' , side5, 'times')
print('you have rolled 6' , side6, 'times')