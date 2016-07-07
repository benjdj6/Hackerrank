#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(1, n+1):
    str = ""
    for j in range(n+1):
        if j < (n+1 - i):
            str += ' '
        else:
            str += '#'
    print str[1:]
    