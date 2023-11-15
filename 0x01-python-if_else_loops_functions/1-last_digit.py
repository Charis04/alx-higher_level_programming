#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    mod = number * -1
    neg = True
else:
    mod = number
    neg = False

while mod >= 10:
    mod %= 10

if neg == True:
    mod *= -1

if mod == 0:
    print("Last digit of {} is {} and is 0".format(number, mod))
elif mod < 6:
    print("Last digit of {} is {} and is less than 6"
            " and not 0".format(number, mod))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, mod))
