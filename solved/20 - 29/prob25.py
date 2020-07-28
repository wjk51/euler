"""Project Euler - Problem 25 (https://projecteuler.net/problem=25)."""

fib_terms = [0, 1]  # list with first two terms of the sequence

# generate fib_terms until a term with 1000-digits is created
while len(str(fib_terms[-1])) < 1000:
    new_term = fib_terms[-1] + fib_terms[-2]  # F(n) = F(n-1) + F(n-2)
    fib_terms.append(new_term)

# print the index of the 1000-digit term
print(fib_terms.index(fib_terms[-1]))
