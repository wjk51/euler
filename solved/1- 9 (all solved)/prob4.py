"""Project Euler - Problem 4 (https://projecteuler.net/problem=4)."""

largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = str(i * j)  # cast to str for char comparison

        if product[0] == product[-1]:
            if product[1] == product[-2]:
                if product[2] == product[-3]:
                    # product is a palindrome -> check if largest
                    if int(product) > largest_palindrome:
                        largest_palindrome = int(product)

print(largest_palindrome)
