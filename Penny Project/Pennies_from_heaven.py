pennies = int(input("How many pennies do you have? "))

import math 
def how_many(pen):
    if pen >= 100:
        dollars = pen / 100
        print("Dollars =", math.trunc(dollars))
    if  pen % 100 >= 25:
        quarters = pen % 100 / 25
        print("Quarters = ", math.trunc(quarters))
    if  pen % 100 % 25 >= 10:
        dimes = pen % 100 % 25 / 10
        print("Dimes = ", math.trunc(dimes))
    if  pen % 100 % 25 % 10 >= 5:
        nickels = pen % 100 % 25 % 10 / 5
        print("Nickels =", math.trunc(nickels))
    if  pen % 100 % 25 % 10 % 5 >= 1:
        penny_s = pen % 100 % 25 % 10 % 5 / 1
        print("Pennies =", math.trunc(penny_s))
    
how_many(pennies)
