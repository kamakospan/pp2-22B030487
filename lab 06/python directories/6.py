# Write Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

for i in range(65, 65+26):
    filename = chr(i)+'.txt' # using chr() function  to convert this ASCII value to the character
    # Open this file in writing mode by passing the first argument as filename and second argument mode as w(Writing mode)
    with open(chr(i) + ".txt", "w") as file:
        file.writelines(chr(i))