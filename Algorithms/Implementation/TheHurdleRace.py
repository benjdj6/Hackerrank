#!/bin/python

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
height = map(int, raw_input().strip().split(' '))
drinks = 0
mx = 0
for i in height:
    if i > mx:
        mx = i
drinks = mx - k
if drinks <= 0:
    print 0
else:
    print drinks
