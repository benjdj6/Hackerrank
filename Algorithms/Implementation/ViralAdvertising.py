# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n = int(raw_input())
m = 5
total = 0
for i in range(n):
    daily = math.floor(m / 2)
    total += int(daily)
    m = daily * 3

print total
