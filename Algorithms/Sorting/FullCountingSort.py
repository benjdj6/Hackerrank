# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
nums = [[] for x in range(100)]
for i in range(n):
    raw = raw_input().split(' ')
    curr_num = int(raw[0])
    curr_s = raw[1]
    if i < n / 2:
        curr_s = "-"
    nums[curr_num].append(curr_s)

for a in nums:
    for s in a:
        print s,
