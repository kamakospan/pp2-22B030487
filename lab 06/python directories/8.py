# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os
import sys

file = r'iwillbedeleted.txt'
pathh = r'C:\Users\miss_\OneDrive\Документы\pp2\lab 6\iwillbedeleted.txt'
isExist = os.path.exists(pathh)
print(isExist)

path = r'C:\Users\miss_\OneDrive\Документы\pp2\lab 6'

accessbarma = os.access("iwillbedeleted.txt", os.R_OK)

if accessbarma == True and isExist == True:
    path1 = os.path.join(path, file)
    os.remove(path1)
