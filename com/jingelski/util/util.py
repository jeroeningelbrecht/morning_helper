import math


def round_half_up(n, decimals=0) -> float:
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
