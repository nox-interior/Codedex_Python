# Calculate the hypothenuse after the Pythagorean theorem: a2+b2=c2

import math

a = int(input('Enter a: '))
b = int(input('Enter b: '))

c = math.sqrt( a ** 2 + b ** 2 )

print("Hypotenuse: " + str(c))

# str converts a value into a string in order to concatenate the output

# Codédex solution


a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2 + b**2) ** 0.5

print(c)