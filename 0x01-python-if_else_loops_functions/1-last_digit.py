#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    neg_number = -(number)
    neg_number = neg_number % 10
    neg_number = -(neg_number)

last_digit = number % 10


if (last_digit == 0):
    print("Last digit of", number, "is", last_digit, "and is 0")

elif (last_digit > 5):
    print("Last digit of", number, "is", last_digit, "and is greater than 5")

elif (last_digit > 0) and (last_digit > 6):
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")

else:
    print("Last digit of", number, "is", neg_number, "and is less than 6 and not 0")
