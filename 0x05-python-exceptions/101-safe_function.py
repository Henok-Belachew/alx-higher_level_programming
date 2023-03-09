#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as err:
        print("Exception: {}".format(err))
        return None
