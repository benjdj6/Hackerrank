#!/bin/python

N = int(raw_input().strip())
for i in range(1, 11):
    tmp = N * i
    print "{} x {} = {}".format(N, i, tmp)
