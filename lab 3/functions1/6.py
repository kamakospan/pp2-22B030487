# Python3 program to reverse a string

# Reverse the letters
# of the word
def reverse(str, start, end):
	# Temporary variable
	# to store character
	temp = ''
	str1 = ""

	while (start <= end):
		# Swapping the first
		# and last character
		temp = str[start]
		str[start] = str[end]
		str[end] = temp
		start+=1
		end-=1
	return str1.join(str)

def reverseWords(s):
	
	word_begin = -1

	# temp is for word boundary
	i = 0

	# STEP 1 of the above algorithm
	while (i < len(s)):

		''' This condition is to make sure that the
				string start with valid character (not
				space) only '''
		if ((word_begin == -1) and (s[i] != ' ')):
			word_begin = i
		if (word_begin != -1 and ((i + 1 == len(s)) or (s[i + 1] == ' '))):
			s = reverse(list(s), word_begin, i)
			word_begin = -1
		i+=1
	''' End of while '''

	# STEP 2 of the above algorithm
	s = reverse(list(s), 0, (len(s) - 1))
	return s

# Driver Code
s =  input()

# Function call
p = reverseWords(list(s))
print(p)

# This code is contributed by akashish__
