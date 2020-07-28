"""Project Euler - Problem 2 (https://projecteuler.net/problem=2)."""

fib_terms = [0, 1]  # list with first two terms of the sequence
even_terms_sum = 0

while fib_terms[-1] < 4000000:
    new_term = fib_terms[-1] + fib_terms[-2]  # F(n) = F(n-1) + F(n-2)
    fib_terms.append(new_term)

    if new_term % 2 == 0:
        even_terms_sum += new_term

print(even_terms_sum)
