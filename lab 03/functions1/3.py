# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(heads, legs):
    koyan=legs/2-heads
    tauyk=heads-koyan
    return [int(koyan), int(tauyk)]

print(solve(35,94))