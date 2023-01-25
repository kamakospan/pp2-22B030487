# global variables

x = "swesome"

def myfunction():
    print ("Python is " + x)

myfunction()

# example 1

x = "awesome" 
def myfunction():
    x = "fantastic"
    print ("Pyhton is " + x)

myfunction()

print("Python is " + x)

# the global keyword
def myfunct():
    global x
    x = "fantastic"

myfunct()

print ("Python is " + x)

# example 2

x = "awesome"

def func():
    global x;
    x = "fantastic"

func()

print("Python is " + x)