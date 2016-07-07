#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    present = 0
    for i in range(n):
        if a[i] <= 0:
            present += 1
    if present < k:
        print "YES"
    else:
        print "NO"

