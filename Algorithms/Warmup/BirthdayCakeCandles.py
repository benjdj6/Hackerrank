#!/bin/python


def birthdayCakeCandles(n, ar):
    maxH = -1
    result = 0
    for h in ar:
        if h > maxH:
            maxH = h
    for h in ar:
        if h == maxH:
            result += 1
    return result


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
