# Enter your code here. Read input from STDIN. Print output to STDOUT
k = map(int, list(raw_input().split()))
food = map(int, list(raw_input().split()))
charge = int(raw_input())
total = 0
for i in range(len(food)):
    if i != k[1]:
        total += food[i]

total = total / 2
diff = charge - total
if diff != 0:
    print diff
else:
    print "Bon Appetit"
