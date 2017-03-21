#!/bin/python

n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    if grade < 38 or grade % 5 < 3:
        print grade
    else:
        print grade + (5 - (grade % 5))
