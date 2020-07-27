"""Project Euler - Problem 1 (https://projecteuler.net/problem=1)."""

sum_of_multiples = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:  # multiple of 3 or 5
        sum_of_multiples += i  # add to sum

print(sum_of_multiples)
