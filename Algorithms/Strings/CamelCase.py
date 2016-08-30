#!/bin/python

import sys


s = list(raw_input().strip())
count = 1
for c in s:
    if c.isupper():
        count += 1
        
print count