# Write a Python program to write a list to a file.

L = ["wasssuuuupppp good dayyy"]

# writing to file
file1 = open('writingtexttothis.txt', 'w')
file1.writelines(L)
file1.close()
