# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import itemgetter

n, m = map(int, raw_input().split())
table = []
for i in range(n):
    table.append(map(int, raw_input().split()))
k = int(raw_input())
table = sorted(table, key=itemgetter(k))
for t in table:
    print " ".join(str(x) for x in t)
