#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


import re

with open("row.txt","r", encoding='utf-8') as rowfile:
    for str in rowfile:
        result = re.findall(r"a[b]{2, 3}", str)
        if(len(result) != 0):
            for i in result:
                print(i)