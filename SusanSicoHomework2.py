"""

SusanSicoHomework2.py

This program via a main function, AskForLetter, asks the user for a letter that
is a single vowel and checks whether the user wants to quit the program or has
entered more than one letter, a number, or a letter that is not a vowel.

The function AskForLetter calls the function IsVowel which call two other functions,
IsLowercaseVowel and IsUppercaseVowel. 

"""

def IsLowercaseVowel(letter):
    
    """This function determines whether the parameter to the function, letter, is a
    lowercase vowel and returns True if it is. """

    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or
        letter == 'u'):
        return True;

def IsUppercaseVowel(letter):

    """This function determines whether the parameter to the function, letter, is an
    uppercase vowel and returns True if it is. """

    if (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or
        letter == 'U'):
        return True;

def IsVowel(letter):

    """This function determines whether the parameter to the function, letter, is a
    vowel by calling two other functions which determine if letter is an uppercase
    or lowercase vowel. The function returns True if letter is a vowel and False if
    it is not. """

    if IsLowercaseVowel(letter):
        return True
    elif IsUppercaseVowel(letter):
        return True
    else:
        return False

def AskForLetter():

    """This function via a while loop repeatedly asks the user for a single letter 
    that is a vowel until the user enters quit or a single vowel.  The while loop 
    asks the user to enter a vowel.  It then goes through a sequence of checking 
    the input: quit is printed to the screen and the program is exited; if the
    length of the input is not 1, the user is told via output to the screen and the
    program continues; if the letter is a number, the user is told via output to the
    screen and the program continues; if the user has entered a single letter, the
    program determines whether the letter is an uppercase or lowercase vowel.  If
    the letter is not a vowel, the user is told via output to the screen and the
    program continues.  Otherwise, the vowel is output to the screen. """

    single_letter = False
    while single_letter == False:
        letter = raw_input("Please enter a single letter that is a vowel: ")
        # Check for quit.
        if letter == "quit":
            print "You have quit the program."
            break
        # Check for a single letter.
        elif len(letter) != 1:
            print "You have not entered a single letter."
            continue
        # Check for a number.
        else:
            try:
                number = int(letter)
                print "You have entered a number instead of a letter."
                continue
            # Check for an uppercase or lowercase vowel.
            # Print the output if the letter is a vowel.
            except:
                if IsVowel(letter) == False:
                    print "The letter you have entered is not a vowel."
                    continue
                else:
                    print "The vowel you have entered is " + letter + "."
                    single_letter = True

# Call the main function.               
AskForLetter()
