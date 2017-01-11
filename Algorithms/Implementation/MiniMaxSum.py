#!/bin/python

a, b, c, d, e = raw_input().strip().split(' ')
a, b, c, d, e = [int(a), int(b), int(c), int(d), int(e)]
l = [a, b, c, d, e]

mx = 0
mn = -1
for n in l:
    if mn == -1 or n < mn:
        mn = n
    if n > mx:
        mx = n
resultmax = a + b + c + d + e - mn
resultmin = a + b + c + d + e - mx
print resultmin, resultmax
