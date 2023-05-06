# Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re
with open("row.txt") as file:
    for text in file:
        result = re.findall(r"[A-Z]{1,}[a-z]{1,}", text)
        if(len(result)!=0):
            for i in result:
                print(i)
                