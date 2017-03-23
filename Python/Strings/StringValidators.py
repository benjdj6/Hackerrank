if __name__ == '__main__':
    s = raw_input()
    s = list(s)
    out = ['False'] * 5
    for c in s:
        if c.isalnum():
            out[0] = 'True'
        if c.isalpha():
            out[1] = 'True'
        elif c.isdigit():
            out[2] = 'True'
        if c.islower():
            out[3] = 'True'
        elif c.isupper():
            out[4] = 'True'
    for i in range(5):
        print out[i]
