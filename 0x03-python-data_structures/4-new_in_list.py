#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return my_list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        newList = my_list.copy()
        newList[idx] = element
        return newList
