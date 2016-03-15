"""

SusanSicoHomework4.py

This is a program that asks the user for the number and names of cities
they would like to visit and then prints two sentences: the first with the
city number and the second with the city number increased by 1.

"""

def AskForNumberOfCities():

    """ Ask the user for the number of cities they would like to visit. """
    
    input = True

    while input == True:
        number_input = raw_input("How many cities would you like to visit? ")
        try:
            # Test for a number.
            city_number = int(number_input)
            # Test for 0.
            if city_number == 0:
                print "Please enter a number greater than 0." 
            else:
                input = False
        except ValueError:
            print "You have not entered an integer value."

    return city_number

def CheckIfAlpha(city_name):

    """ Test whether the input for city name are alpha characters. """

    if city_name.isalpha():
       return True           
    else:
        print "Your input is not the name of a city."
        return False

def DetermineIfCityIsDuplicate(city_input, city_names):

    """ Determine if user has entered the same city twice. """

    i = 0
    city_list = []

    # Convert the city names string into a list.
    city_list = city_names.split()
    while i < len(city_list):
        if city_input == city_list[i]:
            return True
        else:
            i = i + 1

    return False

def AskForCityName(city_number):

    """ Ask the user for the names of cities they would like to visit using 
    the number they input for the number of cities. """  

    i = 0
    city_names = ""

    while i < city_number:
        city_input = raw_input("Please enter the name of one of the cities \
        you would like to visit: ")
        if i == 0:
            if CheckIfAlpha(city_input):
                city_names = city_input
                i = i + 1
        else:
            if CheckIfAlpha(city_input):
                if DetermineIfCityIsDuplicate(city_input, city_names):
                    print "This is a duplicate name."
                # Concatenate the input to the existing string.
                else:
                    city_names = city_names + " " + city_input
                    i = i + 1
                    
    return city_names

def PrintCityNames(city_names):
    
    """ Print the names of the cities and the number of the city in the order 
    they were given by the user as input. """

    i = 0
    city_list = []
    # Start the sentence.
    first_cities_sentence = "You would like to visit"

    # Convert the city names string to a list.
    city_list = city_names.split()
    while i < len(city_list):
        # Initialize and then increment a string for each city number.
        city_number_string = str(i + 1)
        if i == 0:
            # Add the number string for the first city to the sentence.
            first_cities_sentence = first_cities_sentence + " " + city_list[i] + \
            " as city " + city_number_string
            i = i + 1
        else:
            # Add the number string for the remaining cities to the sentence.
            first_cities_sentence = first_cities_sentence + " and " + city_list[i] \
            + " as city " + city_number_string
            i = i + 1
    
    first_cities_sentence = first_cities_sentence + " on your trip."
    print first_cities_sentence
    return first_cities_sentence

def PrintAddOneCityNumSentence(first_city_sentence):

    """ Print a second sentence with the city number incremented by 1. """

    sentence_list = []
    i = 0
    # Initialize the first city number with 2.
    j = 2

    # Convert the first sentence to a list.
    sentence_list = first_city_sentence.split()
    while i < len(sentence_list):
        # If the string element in the list is a digit, add the string of the city number.
        if sentence_list[i].isdigit():
            sentence_list[i] = str(j)
            j = j + 1
            i = i + 1
        else:
            i = i + 1

    # Insert a new first city.
    sentence_list.insert(5, "Amsterdam as city 1 and")
    print " ".join(sentence_list)
    

def CitiesToVisit():

    """ Get the number and names of cities to visit and then print the two sentences. """

    city_number = AskForNumberOfCities()
    city_names = AskForCityName(city_number)
    first_city_sentence = PrintCityNames(city_names)
    PrintAddOneCityNumSentence(first_city_sentence)

#Call the main function.
CitiesToVisit()
    
