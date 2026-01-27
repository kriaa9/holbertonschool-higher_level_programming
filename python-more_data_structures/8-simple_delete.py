#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # .pop(key, None) removes the key if present, returns None if not
    # This avoids errors if the key doesn't exist
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
