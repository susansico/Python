"""

Lab4ExerciseConvertDollarsToEuros

Use of docstring: A docstring is a string
literal tha occurs as the first statement in
a module, function, class, or methos definition.

Program using functions that repeatedly asks the user 
for valid US dollors amount (float) and once the valid
amount given, the prgram will convert that t0 euros
using the current exchange rate at the time of writing.

"""

EURO_CONVERSION_RATE = .78

def GetDollars():
    
    """Asks user for dollar amount as float
    and returns a verfied float."""

    while True:
        us_dollars_input = raw_input("Enter a dollar and cents vale to convert to euros: ")
        try:
            us_dollars = float(us_dollars_input)
        except ValueError:
            print us_dollars, "is not a valid dollar amount. Try again."
            continue
        return us_dollars

def ConvertDollarsToEuros(us_dollars):

    """Converts the parameter us_dollars to euros"""

    euros = us_dollars * EURO_CONVERSION_RATE
    return euros

def Run():

    """Calls functions GetDollars and ConvertDollarsToEuros"""

    verified_us_dollars = GetDollars()
    print "You will be converting", verified_us_dollars, "dollars to euros."
    print verified_us_dollars, "converted to euros is: ", ConvertDollarsToEuros(verified_us_dollars)

Run()
    
