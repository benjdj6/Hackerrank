#!/bin/python

N = int(raw_input().strip())
if N % 2 == 0:
    if N >= 6 and N <= 20:
        print "Weird"
    else:
        print "Not Weird"
else:
    print "Weird"
