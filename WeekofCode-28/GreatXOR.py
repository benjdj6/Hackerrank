#!/bin/python
q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    # your code goes here
    total = 0
    for i in range(x):
        if i ^ x > x:
            total += 1
    print total
