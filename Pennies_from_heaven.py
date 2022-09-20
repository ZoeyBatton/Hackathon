pennies = int(input("How many pennies do you have? "))
print(f"You have {pennies} pennies, that is: ")

import math 
def how_many(pen):
    dollars = pen / 100
    d_remainder = pen % 100
    print("Dollar Bills =", math.trunc(dollars))
    quarters = d_remainder / 25
    q_remainder = d_remainder % 25
    print("Quarters = ", math.trunc(quarters))
    dimes = q_remainder / 10
    dime_remainder = q_remainder % 10
    print("Dimes = ", math.trunc(dimes))
    nickels = dime_remainder / 5
    n_remainder = dime_remainder % 5
    print("Nickels =", math.trunc(nickels))
    penny_s = n_remainder / 1
    print("Pennies =", math.trunc(penny_s))
how_many(pennies)
