#!/bin/python

n = int(raw_input().strip())
score = map(int, raw_input().strip().split(' '))
s_min = -1
s_max = -1
c_min = -1
c_max = -1
for x in score:
    if s_min == -1 or s_min > x:
        s_min = x
        c_min += 1
    if s_max < x:
        s_max = x
        c_max += 1
print c_max, c_min
