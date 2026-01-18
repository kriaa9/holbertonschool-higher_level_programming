#!/usr/bin/python3
"""Print numbers from 00 to 99 separated by comma and space.

Uses zero-padded two-digit formatting {:02d}. All numbers are printed on
one line; the final number (99) has no trailing comma.
"""
for i in range(100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}, ".format(i), end='')
