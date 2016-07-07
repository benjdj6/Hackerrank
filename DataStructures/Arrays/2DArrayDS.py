#!/bin/python

import sys


arr = []
finalMax = -999999999
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
    
for i in range(4):
    row1 = arr[i]
    row2 = arr[i+1]
    row3 = arr[i+2]
    for j in range(4):
        currSum = 0
        currSum = row1[j] + row1[j+1] + row1[j+2]
        currSum += row2[j+1]
        currSum += row3[j] + row3[j+1] + row3[j+2]
        if currSum > finalMax:
            finalMax = currSum
print finalMax