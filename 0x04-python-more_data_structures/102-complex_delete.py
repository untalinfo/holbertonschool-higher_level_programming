#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n_dic = []
    for i, j in a_dictionary.items():
        if j == value:
            n_dic.append(i)
    for k in n_dic:
        del a_dictionary[k]
    return a_dictionary
