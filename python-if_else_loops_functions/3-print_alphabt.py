#!/usr/bin/python3
"""Print the lowercase alphabet except 'e' and 'q'.

Uses a for loop over ASCII codes 97 ('a') to 122 ('z'), with a conditional
to skip 101 ('e') and 113 ('q'). Characters are printed on one line.
"""
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end='')
