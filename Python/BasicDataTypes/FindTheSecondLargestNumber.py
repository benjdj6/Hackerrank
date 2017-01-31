if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    mx = []
    arr.sort()
    for n in arr:
        if not mx:
            mx.append(n)
        elif n > mx[len(mx) - 1]:
            mx.append(n)
    print mx[len(mx) - 2]
