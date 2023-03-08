# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

a = "wassupbro"
a1 = "madam"
# a = str(input())
b = ''.join(reversed(a))
b1 = ''.join(reversed(a1))

if a == b: 
    print("Yea bro Im palindrome")
else:
    print("No bro Im not a palindrome sorry bro")
"""
if a1 == b1: 
    print("Yea bro Im palindrome")
else:
    print("No bro Im not a palindrome sorry bro")
"""