# Program that asks the user for the amount they have in 
# peso,
# soles, and 
# reais 
# and calculates the total in USD.

import math

a = int(input('What do you have left in colombian pesos?: '))
b = int(input('What do you have left in brazilian reais?: '))
c = int(input('What do you have left in peruvian soles?: '))

d = (a*0.00024) + (b*0.21) + (c*0.28)

print("Total USD: " + str(d))
