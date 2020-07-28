"""Project Euler - Problem 13 (https://projecteuler.net/problem=13)."""

# one-hundred 50-digit numbers stored in prob8.txt

import re

f = open("prob13.txt", "r")

sum_of_numbers = 0
for line in f.readlines():
    number = int(re.sub("[^0-9]", "", line))  # remove non-numeric chars
    sum_of_numbers += number  # add number to sum


print(str(sum_of_numbers)[0:10])  # print first 10 digits of sum_of_numbers
