#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    threes = (n - 1) / 3
    fives = (n - 1) / 5
    fifteens = (n - 1) / 15
    threes = 3 * (threes * (threes + 1) / 2)
    fives = 5 * (fives * (fives + 1) / 2)
    fifteens = 15 * (fifteens * (fifteens + 1) / 2)
    
    print threes + fives - fifteens