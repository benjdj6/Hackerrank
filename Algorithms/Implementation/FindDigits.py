#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    nlist = map(int, list(str(n)))
    even = 0
    for d in nlist:
        if d != 0 and n % d == 0:
            even += 1
    print even
