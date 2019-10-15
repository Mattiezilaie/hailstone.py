# Author: Mahtab Zilaie
# Date: 10-15-19
# Description: get return value for hailstone sequence using a function

def hailstone(n):
    """return hailstone sequence from n to 1"""
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
