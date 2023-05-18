#!/usr/bin/python3
"""ALX Interview Prep Module."""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    change = 0
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
    return change if (change > 0 and total == 0) else -1
