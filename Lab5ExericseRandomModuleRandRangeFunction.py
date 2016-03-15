"""

Lab6ExerciseRandomModuleRandRangeFunction.py

"""

import random

def ConvertToType(random_number):

    if random_number == 1:
        return "Heads"
    elif random_number == 2:
        return "Tails"

def CheckSame(coin_one, coin_two):

    if coin_one == coin_two:
        return True
    else:
        return False

def TossCoins():

    """Uses random.randrange(1, 3) to emulate the flip of a coin."""

    coin_one = ConvertToType(random.randrange(1, 3))
    coin_two = ConvertToType(random.randrange(1, 3))

    return(CheckSame(coin_one, coin_two))

def GetSameType():

    toss_counter = 1

    while True:
        if toss_counter == 1:
            print toss_counter, "time(s) tossing the coins."
        if TossCoins() == True:
            print "Both coins are of the same type."
            break
        else:
            toss_counter = toss_counter + 1
            print toss_counter, "times tossing the coins."

GetSameType()

    
