#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("0")
    else:
        sum = 0
        for x in range(arguments):
            sum += int(sys.argv[x + 1])
        print("{}".format(sum))
