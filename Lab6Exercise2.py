"""

Lab6Exercise2.py

"""

def ToLowercase(str):

    return str.lower()

def ToUppercase(str):

    return str.upper()

def SplitWithCommas(str):

    split_string = str.split()
    return ", ".join(split_string)

def ToQuestion(str):

    return str + "?"

def GetSentenceAndManipulateString():

    input = False
    while input == False:
        sentence = raw_input("Please enter a sentence or quit to exit: ")
        if sentence == "quit":
            return
        elif len(sentence) == 0:
            print "You have not entered a sentence."
            continue
        else:
            input = True
            
    lowercase_sentence = ToLowercase(sentence)
    uppercase_sentence = ToUppercase(sentence)
    split_sentence_with_commas = SplitWithCommas(sentence)
    sentence_as_question = ToQuestion(sentence)
    print lowercase_sentence
    print uppercase_sentence
    print split_sentence_with_commas
    print sentence_as_question

GetSentenceAndManipulateString()
    
            
