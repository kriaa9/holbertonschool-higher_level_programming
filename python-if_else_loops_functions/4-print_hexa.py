#!/usr/bin/python3
"""Print numbers 0..98 in decimal and hexadecimal.

Demonstrates formatting with format specifiers: {:d} for decimal and {:x}
for lowercase hexadecimal. Each line shows the decimal and its hex form.
"""
for i in range(99):
    print("{:d} = 0x{:x}".format(i, i))
