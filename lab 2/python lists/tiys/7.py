#accessing list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# there's negative indexing, too
# so the -1 refers to the last element

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# also some range of elements can be taken as follows
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])