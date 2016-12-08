n = int(raw_input())
s = set(map(int, raw_input().split()))
print sum(s)/(len(s) + 0.0)