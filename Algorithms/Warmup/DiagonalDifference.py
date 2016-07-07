#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

sum_1 = 0   
sum_2 = 0
for i in range(n):
    sum_1 += a[i][i]
i=0
for j in range(n-1, -1, -1):
    sum_2 += a[i][j]
    i += 1
print abs(sum_1 - sum_2)