"""Project Euler - Problem 5 (https://projecteuler.net/problem=5)."""


def evenly_divisible_to(n, divisible_to):
    """Return True if n is evenly divisible by the numbers 1:divisble_to."""
    is_divisible = True  # assume True until proven False

    for i in range(1, divisible_to + 1):
        if n % i != 0:  # remainder -> not evenly divisible
            is_divisible = False
            break

    return is_divisible


j = 2520
while not evenly_divisible_to(j, 20):
    j += 2520

print(j)
