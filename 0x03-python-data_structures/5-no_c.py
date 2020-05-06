#!/usr/bin/env python3
def no_c(my_string):
    n = ""
    for c in my_string:
        if c not in "cC":
            n = n + c
    return (n)
