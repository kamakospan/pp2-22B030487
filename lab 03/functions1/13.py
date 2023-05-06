# 12. Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:

def histogram(values):
    curr = '*'
    for val in values:
        if val != 0:
            curr = curr * val
        else:
            curr = ''
        print(curr)
        curr = '*'


# histogram([1, 0, 2, 0, 3])