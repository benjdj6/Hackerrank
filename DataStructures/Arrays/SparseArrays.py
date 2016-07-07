# Enter your code here. Read input from STDIN. Print output to STDOUT
slist = []
strings = int(raw_input())
for i in range(strings):
    slist.append(raw_input())
queries = int(raw_input())
for q in range(queries):
    curr = raw_input()
    cntr = 0
    for s in slist:
        if curr == s:
            cntr += 1
    print cntr