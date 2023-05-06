# Write a Python program to split a string at uppercase letters.

import re

with open("row.txt") as file:
    for text in file:
        result = re.split(r"[A-Z]",text)
        if(len(result)!=0):
            for i in result:
                print(i)

