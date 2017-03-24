from itertools import permutations

s, k = raw_input().split(' ')
k = int(k)
perm = list(permutations(s, k))
perm.sort()
for p in perm:
    print ''.join(p)
