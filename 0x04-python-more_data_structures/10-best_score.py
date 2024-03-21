#!/usr/bin/python3
def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key_big_val = list(a_dictionary.keys())[0]
    big = a_dictionary[key_big_val]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            key_big_val = k
    return (key_big_val)
