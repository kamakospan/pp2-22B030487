# Write a Python program to test whether a given path exists or not. 
# If the path exist find the filename and directory portion of the given path.

import os

# path = r'C:\Users\miss_\OneDrive\Документы\pp2\lab 6\python directories\iwillbedeleted.txt'
path = r'C:\Users\miss_\OneDrive\Документы\pp2\lab 6\python directories\iwllbedeleted.txt'

isExist = os.path.exists(path)

if isExist == True: 
    print(os.path.basename(path))
else:
    print("File does not exist so I cant find the name of it bro")
    
    
    
    
    # The base name in the given path can be obtained using the built-in Python function os.path.basename(). 
    #The function path.basename() accepts a path argument and returns the base name of the pathname path.

