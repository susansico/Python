"""

SusanSicoHomework3.py

Get three words from user and convert to Pig Latin

"""

# Define a list of vowels for words that begin with a vowel
VOWELS = ['a','e','i','o','u']

def ToLowercase(string):

    """Convert a string to lowercase."""

    return string.lower()

def StringToList(string):

    """Convert a string to a list."""

    return string.split()

def AddWordToString(string, word):

    """Add a word to a string by concatenating the word to string.
    For an empty string, just add the word, otherwise add the
    word to the string separated with a space."""

    if string == "":
        string = word
    else:
        string = string + " " + word

    return string

def WordsToPigLatinString(list):

    """Convert each of three words in the list to Pig Latin. If 
    the word starts with a vowel, add hay to the end of the word,
    otherwise move the first letter of the word to the end of
    the word and add ay."""

    counter = 0
    pig_latin_string = ""
    
    while counter < 3:
        word = list[counter]
        if word[0] in VOWELS:
            pig_latin_word = word + "hay"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_string = AddWordToString(pig_latin_string, pig_latin_word)
        counter = counter + 1

    return pig_latin_string

def PrintString(string):

    """Print the string."""

    print string
                   
def ConvertWordsToPigLatin(word_string):

    """Convert a string to lowercase, convert the lowercase
    string to a list, and convert each of the words in the list 
    to Pig Latin while adding the word to a string."""

    word_list = []
    
    lowercase_string = ToLowercase(word_string)
    word_list = StringToList(lowercase_string)
    pig_latin_string = WordsToPigLatinString(word_list)

    return pig_latin_string
    
    
def GetWords():

    """Get three words from the user and convert the words to Pig
    Latin until user enters quit. Print the Pig Latin string. """

    input = True;

    while input == True:
        input_string = raw_input("Please enter three words. Please enter quit when you are done: ")
        if (input_string == "quit"):
            input = False
        elif len(input_string) == 0:
            print "You have not entered three words."
        else:
            pig_latin_string = ConvertWordsToPigLatin(input_string)
            PrintString(pig_latin_string) 

GetWords()
