#!/usr/bin/python3

"""
Module that contains a method that calculates the
fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    str = 'H'  # Xter to be formed
    operations = 0
    factor = 2# Initialize factor

    if n < 0:
        return 0  # Return 0 if n is negative

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
