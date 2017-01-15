#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    b, w = raw_input().strip().split(' ')
    b, w = [long(b), long(w)]
    x, y, z = raw_input().strip().split(' ')
    x, y, z = [long(x), long(y), long(z)]
    result = 0
    if z + y < x:
        result = y * w
        result += (y + z) * b
    elif z + x < y:
        result = x * b
        result += (x + z) * w
    else:
        result = x * b
        result += y * w
    print result
