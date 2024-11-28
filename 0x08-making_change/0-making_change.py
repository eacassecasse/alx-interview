#!/usr/bin/python3


def makeChange(coins, total):
    """
    Computes the amount of coins needed to make a change
    :param coins: The list of available coins
    :param total: The amount to change
    :return: The amount of coins needed to make a change,
    -1 if the coins does not suffice a change
    """
    remain = total
    amount_coins = 0
    coins = sorted(coins)
    pos = len(coins) - 1

    if total <= 0:
        return 0

    while remain > 0:
        if remain >= coins[pos]:
            amount_coins += 1
            remain -= coins[pos]
        else:
            if pos > 0:
                pos -= 1
            else:
                return -1
    return amount_coins
