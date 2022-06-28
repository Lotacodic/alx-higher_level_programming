#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) > 96 and ord(upper) < 123:
            upper = chr(ord(upper) - 32)
        print("{}".format(upper), end="")
    print("")
