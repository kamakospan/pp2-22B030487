"""Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""

def fahrenheit():
    print ("temperature in centigrade = ", 5 / 9 * (temp - 32))

temp = float(input())
fahrenheit()