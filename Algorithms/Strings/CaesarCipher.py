#!/bin/python

import sys


n = int(raw_input().strip())
s = list(raw_input().strip())
k = int(raw_input().strip())

if k >= 26:
    k = k % 26
for i in range(len(s)):
    if s[i].isalpha():
        tmp = chr(ord(s[i]) + k)
        if s[i].islower() and ord(tmp) > 122:
            offset = ord(tmp) - 122
            s[i] = chr(ord('a') + offset - 1)
        elif s[i].isupper() and ord(tmp) > 90:
            offset = ord(tmp) - 90
            s[i] = chr(ord('A') + offset - 1)
        else:
            s[i] = tmp
print "".join(s)

