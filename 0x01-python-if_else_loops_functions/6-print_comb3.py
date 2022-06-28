#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{0}{1}".format(num1, num2))
        else:
            print("{0}{1}".format(num1, num2), end=", ")
