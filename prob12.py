"""Project Euler - Problem 12 (https://projecteuler.net/problem=12)."""

from math import sqrt


def nth_triangular_number(n):
    return int(n * (n + 1) / 2)
