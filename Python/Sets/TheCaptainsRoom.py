# Enter your code here. Read input from STDIN. Print output to STDOUT


def findCap(rooms):
    half1 = set(rooms[:len(rooms) / 2])
    half2 = set(rooms[(len(rooms) / 2) + 1:])
    result = list(half1.symmetric_difference(half2))
    if len(result) > 1:
        for i in result:
            if i in half1:
                return findCap(list(half1))
            else:
                return findCap(list(half2))
    else:
        return result[0]


k = int(raw_input())
rooms = map(int, raw_input().split())
print findCap(rooms)
