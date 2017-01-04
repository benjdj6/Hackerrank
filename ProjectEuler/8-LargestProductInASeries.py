#!/bin/python

import sys
import operator


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = map(int, list(raw_input()))
    result = 0
    for i in range(k, n):
        curr = reduce(operator.mul, num[i-k:i])
        if result < curr:
            result = curr
    print result