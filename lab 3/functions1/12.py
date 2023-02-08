import random
import math

name = input("Hello! What is your name? ")
print ("Well, ", name, "I am thinking of a number between 1 and 20.")
print ("Take a guess.")

x = random.randint(1, 20)

count = 0

guess = int(input())

if guess < int(x):
    count += 1
    print("Your guess is too low")
    
elif guess > int(x):
    count += 1
    print("Your guess is too high")
    
elif guess == int(x):
    print("Good job, KBTU! You guessed my number in ", count, "guesses!")

