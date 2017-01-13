#!/bin/python

n, t = raw_input().strip().split(' ')
n, t = [int(n), int(t)]
width = map(int, raw_input().strip().split(' '))
for a0 in xrange(t):
    i, j = raw_input().strip().split(' ')
    i, j = [int(i), int(j)]
    min_width = 3
    for x in range(i, j + 1):
        if width[x] < min_width:
            min_width = width[x]
    print min_width
