# Implement a generator that returns all numbers from (n) down to 0.

import math

def numbers(max):
    i = max
    while i != 0:
        yield i
        i -= 1

max = int(input())

for i in numbers(max):
    print(i)
