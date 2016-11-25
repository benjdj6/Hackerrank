#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
acount = 0
ocount = 0
for n in apple:
    if n + a >= s and n + a <= t:
        acount += 1
print acount
for n in orange:
    if n + b <= t and n + b >= s:
        ocount += 1
print ocount