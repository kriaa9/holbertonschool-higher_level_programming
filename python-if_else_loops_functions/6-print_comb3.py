#!/usr/bin/python3
"""Print all combinations of two different digits (01 to 89).

Nested loops generate pairs where the second digit is greater than the
first to avoid duplicates like 00, 11, or reversed pairs like 21 after 12.
Commas separate pairs; the last pair (89) ends with a newline only.
"""
for a in range(10):
    for b in range(a + 1, 10):
        if b == 9 and a == 8:
            print("{:d}{:d}".format(a, b))
        else:
            print("{:d}{:d}".format(a, b), end=", ")
