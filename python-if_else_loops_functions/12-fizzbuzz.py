#!/usr/bin/python3
"""Provide `fizzbuzz()` to print numbers 1..100 with rules.

Multiples of 3 print "Fizz", multiples of 5 print "Buzz", and multiples
of both print "FizzBuzz". Each element is followed by a space.
"""
def fizzbuzz():
    """Print numbers from 1 to 100 with Fizz, Buzz, FizzBuzz rules.

    For multiples of 3: print Fizz
    For multiples of 5: print Buzz
    For multiples of both 3 and 5: print FizzBuzz
    Otherwise: print the number
    Each element is followed by a space.
    """
    # Loop from 1 to 100 inclusive
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
