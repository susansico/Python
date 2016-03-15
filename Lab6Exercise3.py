"""

Lab6Exercise3

"""

def LenList(list):

    return len(list)

import random
def GetRandomNumber(first_range_number, second_range_number):

    return random.randrange(first_range_number, second_range_number)

def RemoveRandomElementFromList(list, index):

    list_element = list[index]
    list.remove(list_element)
    print list

def GetListAndManipulateElements():

    user_list = []
    input = True

    while input == True:
        user_input = raw_input("Please enter items for a list. Please type quit when you are done: ")
        if user_input == "quit":
            input = False
        elif len(user_input) == 0:
            print "You have not entered an item for the list."
        else:
            user_list.append(user_input)

    user_list_len = LenList(user_list)
    random_number = GetRandomNumber(1, user_list_len + 1)
    if random_number == 0:
        print "The random number is equal to 0."
    else:
        RemoveRandomElementFromList(user_list, random_number - 1)

GetListAndManipulateElements()

    
    
