# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

import math 

def evensmaker(n):
    i = 1
    while(i <= n):
        if i % 2 == 0:
            yield i
        i += 1

n = int(input())
for i in evensmaker(n):
    print(i)

