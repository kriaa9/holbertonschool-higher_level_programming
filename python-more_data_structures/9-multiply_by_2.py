#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Dictionary comprehension to create a new dict with updated values
    return {key: value * 2 for key, value in a_dictionary.items()}
