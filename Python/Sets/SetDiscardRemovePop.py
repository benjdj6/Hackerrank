n = input()
s = set(map(int, raw_input().split()))
for i in range(int(raw_input())):
    c = raw_input().split()
    if c[0] == "remove":
        s.remove(int(c[1]))
    elif c[0] == "discard":
        s.discard(int(c[1]))
    elif c[0] == "pop":
        s.pop()
print sum(s)
