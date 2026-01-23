#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Add (0, 0) to ensure we always have enough elements
    ta = tuple_a + (0, 0)
    tb = tuple_b + (0, 0)
    # Return the sum of the first two elements
    return (ta[0] + tb[0], ta[1] + tb[1])
