#!/usr/bin/python3
"""Print the lowercase English alphabet without a newline.

Demonstrates a simple for loop, ASCII codes, and chr() to convert integer
code points to characters. Each character is printed without a newline by
using end=''.
"""
for i in range(97, 123):
    print("{}".format(chr(i)), end='')
