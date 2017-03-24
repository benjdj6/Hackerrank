from itertools import combinations_with_replacement

s, k = list(raw_input().split(' '))
k = int(k)
out = list(combinations_with_replacement(sorted(s), k))
for o in out:
    print ''.join(o)
