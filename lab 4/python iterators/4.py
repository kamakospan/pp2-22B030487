# Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    i = a
    while i <=b:
        yield i**2
        i += 1

a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)