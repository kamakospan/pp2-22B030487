import re

with open("row.txt","r", encoding='utf-8') as rowfile:
    for str in rowfile:
        result = re.findall(r"a[b]{0,}", str)
        if(len(result)!=0):
            for i in result:
                print(i)

# s = str(input())
# result = re.search(r'[ab]\b', s) 
# print(result)
"""
# Solution
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))`
"""