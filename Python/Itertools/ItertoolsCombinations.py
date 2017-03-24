from itertools import combinations

s, k = raw_input().split(' ')
k = int(k)
comb = []
for i in range(1, k + 1):
    tmp = list(combinations(sorted(s), i))
    comb += tmp
for c in comb:
    print ''.join(c)
