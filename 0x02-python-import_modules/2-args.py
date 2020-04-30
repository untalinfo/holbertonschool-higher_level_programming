#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) - 1 > 0:
        if len(argv) - 1 == 1:
            print("{} argument:".format(len(argv) - 1))
        else:
            print("{} argument:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
    else:
        print("0 arguments.")
