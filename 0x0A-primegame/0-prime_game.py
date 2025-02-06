#!/usr/bin/python3
""" This module defines a function isWinner(). """


def isWinner(x, nums):
    """
    Determines who is the winner of the prime game with "x" rounds.
    :param x: the number of rounds to play
    :param nums: the list of number that limits each round
    :return: The actual winner
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda m: m, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
