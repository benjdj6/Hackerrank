#!/bin/python

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "quarter",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "half"
}


def convertMinutes(m):
    if m in numbers:
        result = numbers[m]
    else:
        singles = m % 10
        tens = m - singles
        result = "{0} {1}".format(numbers[tens], numbers[singles])
    if m % 15 != 0:
        result += " minutes"
    return result


h = int(raw_input().strip())
m = int(raw_input().strip())

if m > 30:
    if h == 12:
        h = 0
    h += 1
    m = 60 - m
    hours = numbers[h]
    minutes = convertMinutes(m)
    print "{0} to {1}".format(minutes, hours)
else:
    hours = numbers[h]
    if m == 0:
        print "{0} o' clock".format(hours)
    else:
        minutes = convertMinutes(m)
        print "{0} past {1}".format(minutes, hours)
