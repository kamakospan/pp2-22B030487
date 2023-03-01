# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
with open("row.txt") as file:
    for text in file:
        result = re.sub(r"[, .]", ":", text)
        if(len(result)!=0):
            for i in result:
                print(i)