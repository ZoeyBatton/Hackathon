pennies = int(input("How many pennies do you have? "))

import math 

def dollars(pen):
    pen_remainder = pen % 100
    pen_dollars = (pen / 100)
    pen_quarters = (pen_remainder / 25)
    pen_q_remainder = ()
    pen_dimes = (pen_quarters / 10)
    print(math.trunc(pen_remainder))
    print(math.trunc(pen_dollars))
    print(math.trunc(pen_quarters))
    print(math.trunc(pen_dimes))
dollars(pennies)