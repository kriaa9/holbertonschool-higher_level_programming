#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    
    # Assume the first one is the biggest to start
    big = my_list[0]
    
    for i in my_list:
        if i > big:
            big = i
            
    return big
