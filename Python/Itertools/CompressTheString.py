from itertools import groupby

s = raw_input()
for k, g in groupby(s):
    print (len(list(g)), int(k)),
