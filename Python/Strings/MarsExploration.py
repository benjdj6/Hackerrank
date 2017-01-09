#!/bin/python

import sys


S = list(raw_input().strip())
altered = 0
for i in range(2, len(S), 3):
    if S[i] != 'S':
        altered += 1
    if S[i - 1] != 'O':
        altered += 1
    if S[i - 2] != 'S':
        altered += 1
print altered
