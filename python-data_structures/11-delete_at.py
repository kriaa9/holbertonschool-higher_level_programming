#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if index is valid (not negative and not out of range)
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
