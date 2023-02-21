# Create a generator that generates the squares of numbers up to some number N.
import math 

def squaremaker(N):
    n = 1
    while(n <= N):
        yield n**2
        n = n + 1

N = int(input())
for squares in squaremaker(N):
    print(squares)