"""Project Euler - Problem 10 (https://projecteuler.net/problem=10)."""


from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    prime = True  # assume prime until proven otherwise

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # factor found -> not prime
            prime = False
            break

    return prime


sum_of_primes = 0
j = 2  # first prime

while j < 2000000:
    if is_prime(j):
        sum_of_primes += j
    j += 1

print(sum_of_primes)
