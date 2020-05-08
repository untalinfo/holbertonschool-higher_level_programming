#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div = 0
    if not my_list:
        return 0
    else:
        for i in my_list:
            sum += i[1] * i[0]
            div += i[1]
        return sum/div
