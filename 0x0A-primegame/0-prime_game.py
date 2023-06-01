#!/usr/bin/python3
"""ALX SE Interview Prep Module."""

class PrimeGamer:
    def __init__(self):
        self.players = ('Maria', 'Ben')

    def isPrime(self, num):
        if num == 1:
            return False
        for n in range(2, (num // 2) + 1):
            if num % 2 == 0:
                return False
        return True

    def choosePrime(self, arr):
        for n in arr:
            if self.isPrime(n):
                return n
        return False

    def removeMultiples(self, n, arr):
        out = []
        for num in arr:
            if num % n != 0:
                out.append(num)
        return out

    def getPlayer(self, idx):
        if idx % 2 == 1:
            return self.players[0]
        return self.players[1]


def isWinner(x, nums):
    """Solve the Prime Game Challenge."""
    stats = {'Maria': 0, 'Ben': 0}
    prime = PrimeGamer()

    for r in range(x):
        arr = list(range(1, nums[r] + 1))
        for i in arr:
            player = prime.getPlayer(i)
            p_val = prime.choosePrime(arr)
            if p_val:
                arr = prime.removeMultiples(p_val, arr)
            else:
                winner = prime.getPlayer(i + 1)
                stats[winner] = stats[winner] + 1
                break
    if stats['Maria'] == stats['Ben']:
        return None
    return 'Maria' if stats['Maria'] > stats['Ben'] else 'Ben'
