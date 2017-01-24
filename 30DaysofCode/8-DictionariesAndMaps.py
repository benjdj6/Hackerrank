# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
book = {}
for i in range(n):
    s = raw_input().split(' ')
    book[s[0]] = s[1]
while True:
    q = raw_input()
    if q in book:
        print "{0}={1}".format(q, book[q])
    else:
        print "Not found"
