"""Project Euler - Problem 20 (https://projecteuler.net/problem=20)."""


def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


# get result of 100! and cast to str for looping through digits
fac_100 = str(recursive_factorial(100))
sum_of_digits = 0

for digit in fac_100:
    sum_of_digits += int(digit)  # cast back to int for addition

print(sum_of_digits)
