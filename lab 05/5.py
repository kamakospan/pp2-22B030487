#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


import re
with open("row.txt") as file:
    for text in file:
        result = re.findall(r"a[^ ]{0,}b", text)
        if(len(result)!=0):
            for i in result:
                print(i)

# ^   Matches the beginning