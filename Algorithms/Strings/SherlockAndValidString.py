# Enter your code here. Read input from STDIN. Print output to STDOUT

s = list(raw_input())
repeats = {}

for i in range(len(s)):
    if s[i] in repeats:
        repeats[s[i]] += 1
    else:
        repeats[s[i]] = 1

minimum = 0
alter = 0
match = 0
for key, value in repeats.iteritems():
    if minimum == 0:
        minimum = value
    elif value < minimum:
        if value == 1:
            alter += 1
        else:
            alter += minimum - value
            alter += match
            match = 0
            minimum = value
    elif value > minimum:
        alter += value - minimum
    else:
        match += 1
    if alter > 1:
        break
        
if alter > 1:
    print "NO"
else:
    print "YES"