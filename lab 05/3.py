# Write a Python program to find sequences of lowercase letters joined with a underscore.

"""
import re

s = str(input())
result = re.findall(r'[a-z]{1, }[_]{1, }[a-z]{1, }', s)

print(result)
"""

import re
with open("row.txt") as file:
    for text in file:
        result = re.findall(r"[a-z]{1,}[_]{1,}[a-z]{1,}", text)
        if(len(result)!=0):
            for i in result:
                print(i)