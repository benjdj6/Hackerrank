# Enter your code here. Read input from STDIN. Print output to STDOUT
l = int(raw_input())
a = map(int, list(raw_input().split()))

count = {}

for i in range(l):
    if a[i] not in count:
        count[a[i]] = 1
    else:
        count[a[i]] += 1
mx = 0
for key, val in count.iteritems():
    if val > mx:
        mx = val

print l - mx
