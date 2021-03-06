"""Project Euler - Problem 3 (https://projecteuler.net/problem=3)."""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    prime = True  # assume prime until proven otherwise

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # factor found -> not prime
            prime = False
            break

    return prime


largest_prime_factor = 0

for j in range(1, int(sqrt(600851475143) + 1)):
    if 600851475143 % j == 0:
        if is_prime(j):
            if j > largest_prime_factor:
                largest_prime_factor = j

print(largest_prime_factor)
