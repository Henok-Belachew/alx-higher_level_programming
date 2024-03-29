#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            rst = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            rst = 0
        except ZeroDivisionError:
            print("division by 0")
            rst = 0
        except IndexError:
            print("out of range")
            rst = 0
        finally:
            result.append(rst)
    return result
