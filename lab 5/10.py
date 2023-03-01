# Write a Python program to convert a given camel case string to snake case.

import re
text = "ThisProgramTurnsThisStringIntoSnakeCase"
result = re.findall(r"[A-Z][a-z]*", text)
snake_case=[]
for i in result:
    snake_case.append(i.lower())
print('_'.join(snake_case))