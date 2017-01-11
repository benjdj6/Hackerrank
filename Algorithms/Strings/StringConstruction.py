#!/bin/python

n = int(raw_input().strip())
for a0 in xrange(n):
    chars = {}
    unique = 0

    s = list(raw_input().strip())
    for i in range(len(s)):
        if s[i] not in chars:
            unique += 1
            chars[s[i]] = 1
    print unique
