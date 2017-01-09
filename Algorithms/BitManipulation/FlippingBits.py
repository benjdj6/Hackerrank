# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())

for i in range(t):
    n = "{0:b}".format(int(raw_input()))
    n = n.zfill(32)
    n = list(n)
    for j in range(len(n)):
        if n[j] == '0':
            n[j] = '1'
        elif n[j] == '1':
            n[j] = '0'
    n = "".join(n)
    print int(n, 2)