#!/bin/python3

import sys

numbers = [2, 8]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    while numbers[len(numbers)-1] < n:
        i = (4 * numbers[len(numbers)-1]) + numbers[len(numbers)-2]
        numbers.append(i)
    for num in numbers:
        if num <= n:
            sum += num
        else:
            break
    print(sum)