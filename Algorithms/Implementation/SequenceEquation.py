n = int(raw_input())
p = map(int, raw_input().split(' '))
for i in range(1, n + 1):
    print p.index(p.index(i) + 1) + 1
