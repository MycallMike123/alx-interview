#!/usr/bin/python3

"""
Module to make change for a given amount of money
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0

    if coins is None or len(coins) == 0:
        return -1

    # Sort coins in descending order
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        # move to the next coin when current coin cannot be used
        while total >= coin:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count
