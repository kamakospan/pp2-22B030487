# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os
import sys

path = r'C:\Users\miss_\OneDrive\Документы\pp2\lab 6\python directories\iwillbedeleted.txt'
path1 = os.access(__file__, os.F_OK)
print("Does the path exist? ", path1)

path1 = os.access(__file__, os.R_OK)
print("Can you read the file:", path1)

path1 = os.access(__file__, os.W_OK)
print("Can you write the file:", path1)

path1 = os.access(__file__, os.X_OK)
print("Can it be executed:", path1)
