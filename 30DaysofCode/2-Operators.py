# Enter your code here. Read input from STDIN. Print output to STDOUT
rawMeal = float(raw_input())
tip = float(raw_input())
tax = float(raw_input())
total = rawMeal
total += rawMeal * (tip / 100)
total += rawMeal * (tax / 100)
print "The total meal cost is {} dollars.".format(int(round(total)))
