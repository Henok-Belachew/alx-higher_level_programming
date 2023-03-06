#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None
    else:
        values = sorted(a_dictionary.values(), reverse=True)
        for key, value in a_dictionary.items():
            if value == values[0]:
                return key
