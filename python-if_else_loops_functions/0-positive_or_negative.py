#!/usr/bin/python3
"""Classify a random integer as positive, zero, or negative.

This script demonstrates basic control flow with if/elif/else. A random
integer in the range [-10, 10] is generated, then a message is printed to
describe whether the number is positive, zero, or negative.
"""
import random

number = random.randint(-10, 10)
# If the number is greater than 0, it is positive
if number > 0:
    print(f"{number} is positive")
# If equal to 0, it is zero
elif number == 0:
    print(f"{number} is zero")
# Otherwise (less than 0), it is negative
else:
    print(f"{number} is negative")
