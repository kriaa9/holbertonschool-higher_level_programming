#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if b == 9 and a == 8:
            print("{:d}{:d}".format(a, b))
        else:
            print("{:d}{:d}".format(a, b), end=", ")
