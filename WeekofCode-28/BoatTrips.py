#!/bin/python
n, c, m = raw_input().strip().split(' ')
n, c, m = [int(n), int(c), int(m)]
p = map(int, raw_input().strip().split(' '))
t_cap = c * m
poss = "Yes"
for i in p:
    if i > t_cap:
        poss = "No"
        break
print poss
