from collections import Counter

x = int(raw_input())
sizes = Counter(map(int, raw_input().split(' ')))
n = int(raw_input())
total = 0
for i in range(n):
    s, p = map(int, raw_input().split(' '))
    if s in sizes and sizes[s] > 0:
        sizes[s] -= 1
        total += p
print total
