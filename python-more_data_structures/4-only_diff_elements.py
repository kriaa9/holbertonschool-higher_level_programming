#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # The ^ operator returns the symmetric difference
    # (elements in set_1 OR set_2, but not both)
    return set_1 ^ set_2
