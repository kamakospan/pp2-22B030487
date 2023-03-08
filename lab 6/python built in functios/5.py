# Write a Python program with builtin function that returns True if all elements of the tuple are true.

# a = list(input())
# b = tuple(input())

a = (12, 15, True, "Hello", 'World', [12,1,3])
b = ("", '', 0,[])

print(all(a)) # TRUE
print(all(b)) # FALSE

"""
The Python all() function returns true if all the elements of a given iterable are True 
otherwise it returns False. 
It also returns True if the iterable object is empty. 
Sometimes while working on some code 
if we want to ensure that user has not entered a False value then we use the all() function."""