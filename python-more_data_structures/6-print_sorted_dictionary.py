#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate through keys sorted alphabetically
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
