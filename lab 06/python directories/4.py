# Write a Python program to count the number of lines in a text file.

with open(r"countmylines.txt", 'r') as fp:
	for count, line in enumerate(fp):
		pass
print('Total Number of lines:', count + 1)
