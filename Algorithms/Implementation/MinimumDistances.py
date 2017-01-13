#!/bin/python

n = int(raw_input().strip())
A = map(int, raw_input().strip().split(' '))
vals = {}
diff = -1
for i in range(n):
    if A[i] in vals:
        if diff == -1 or i - vals[A[i]] < diff:
            diff = i - vals[A[i]]
        vals[A[i]] = i
    else:
        vals[A[i]] = i
print diff
