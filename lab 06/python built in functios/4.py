"""
Write a Python program that invoke square root function after specific milliseconds.

Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858"""

import time
import math

n = int(input("Enter ur number: "))
ms =float(input("Enter the milliseconds: "))

time.sleep(ms/1000)
print("It took me {} ms, the square root is {}".format(ms,math.sqrt(n)))