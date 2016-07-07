# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(raw_input())
for t in range(tests):
    s = raw_input()
    s = list(s)
    counter = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
    print counter