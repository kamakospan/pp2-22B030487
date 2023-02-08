# Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

s = str(input())
r = s[::-1]

if s == r:
    print("yes, it's a palindrome")
else:
    print("no, not a palindrome")