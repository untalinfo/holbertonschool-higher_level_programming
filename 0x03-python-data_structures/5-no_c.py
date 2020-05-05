#!/usr/bin/env python3
def no_c(my_string):
    n = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            n = n + i
    return (n)
