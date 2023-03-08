# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

a = str(input())
# a = "ThisProgramCountsUPPERandlowercaseLetters"
# uppercase: TPCUPPERL - 9
# lowercase: hisrogramountsandlowercaseetters - 32

count_u = 0
count_l = 0

for i in a:
    if(i.islower() == True):
        count_l += 1
    elif(i.isupper() == True):
        count_u += 1

print("Count of uppercase letters is ", count_u)
print("And count of lowercase letters is ", count_l)