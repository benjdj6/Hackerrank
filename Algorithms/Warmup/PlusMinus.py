#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0.0
neg = 0.0
zero = 0.0
for i in range(n):
    if arr[i] > 0:
        pos += 1
    elif arr[i] < 0:
        neg += 1
    else:
        zero += 1
print pos/n
print neg/n
print zero/n