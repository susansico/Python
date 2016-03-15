"""

lab8_exercise_homework2_solution_with_lists_module.py

"""

lowercase_vowel_list = ['a', 'e', 'i', 'o', 'u']
uppercase_vowel_list = ['A', 'E', 'I', 'O', 'U']

def IsLowercaseVowel(letter):

    if letter in lowercase_vowel_list:
        return True
    else:
        return False

def IsUppercaseVowel(letter):

    if letter in uppercase_vowel_list:
        return True
    else:
        return False

def IsVowel(letter):

    lowercase = IsLowercaseVowel(letter)

    uppercase = IsUppercaseVowel(letter)

    if lowercase == True or uppercase == True:
        return True
    else:
        return False


def AskForLetter():

    ask = True

    while ask == True:
        input = raw_input("Please input a single letter. Type quit to exit: ")
        if input == "quit":
            ask = False
        else:
            if len(input) == 1:
                vowel = IsVowel(input)
                if vowel == True:
                    print input, "is a vowel."
                    ask = False
            else:
                print "You did not enter a single letter."

# Needed if file being called from commandline or run in IDLE
if __name__ == '__main__':
    AskForLetter()
        
