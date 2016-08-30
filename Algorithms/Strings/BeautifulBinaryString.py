#!/bin/python

import sys


n = int(raw_input().strip())
B = list(raw_input().strip())
count = 0
i = 2
while i < len(B):
    if B[i-2] == '0' and B[i-1] == '1' and B[i] == '0':
        count += 1
        i += 3
    else:
        i += 1
print count