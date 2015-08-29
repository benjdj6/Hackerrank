# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(t, 0, -1):
    coord = raw_input().split()
    x1 = int(coord[0])
    y1 = int(coord[1])
    x2 = int(coord[2])
    y2 = int(coord[3])
    
    x1 = (x2 - x1) + x2
    y1 = (y2 - y1) + y2
    
    print "{} {}".format(x1, y1)