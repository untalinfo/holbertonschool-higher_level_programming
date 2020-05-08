#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        all_values = list(a_dictionary.values())
        all_keys = list(a_dictionary.keys())
        return all_keys[all_values.index(max(all_values))]
    else:
        return None
