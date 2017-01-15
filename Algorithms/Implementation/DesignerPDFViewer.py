#!/bin/python

h = map(int, raw_input().strip().split(' '))
word = raw_input()
maxh = 0
for c in word:
    maxh = max(maxh, h[ord(c) - ord('a')])

print(maxh * len(word))
