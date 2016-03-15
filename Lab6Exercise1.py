'''

lab6Exercise1.py

'''

def AskForNumbers():

    """ Return a list of numbers given by user."""

    number_list = []
    input = True

    while input == True:
        number_input = raw_input("Please input a number. Type quit to end: ")
        if number_input == "quit":
            input = False
            break
        try:
            number = float(number_input)
            number_list.append(number)
        except ValueError:
            print number_input + " is not a valid number"
            continue
        
    return number_list

def SortNumbers():

    """Makes call to AskForNumbers and sorts list of numbers returned"""
    
    number_list = AskForNumbers()

    # sort the numbers if length of list greater than zero
    if len(number_list) > 0:
        number_list.sort(None, None, True)
        print "The list of numbers sorted is", number_list

SortNumbers()
