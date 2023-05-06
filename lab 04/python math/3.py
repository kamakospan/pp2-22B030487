import math

n = float(input())
l = float(input())

x = (math.radians(180))/n
ctg = 1/(math.tan(x))

print( 0.25 * n * (l * l) * ctg)

