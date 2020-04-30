#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    res = 0
    if len(argv) - 1 > 0:
        if len(argv) - 1 == 1:
            print("{}".format(int(argv[1])))
        else:
            for i in range(len(argv) - 1):
                res = res + int(argv[i + 1])
            print(res)
    else:
        print(0)
