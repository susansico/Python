"""

Lab8Exercise1.py

"""

def Minimum(list):

    return min(list)

def Maximum(list):

    return max(list)

def CalculateAverage(list):

    return sum(list) / len(list)

"""def AppendToList(list, new_list):

    i = 0

    length = len(new_list)
    
    for i < length:
        list.append(new_list[i])

    return list"""

def SortList(list):

    return sorted(list)

def PrintResults(ages, minimum_age, maximum_age, average_age, sorted_list):

    print 'The original input list of ages are:',ages

    print 'The minimum age is:', minimum_age

    print 'The maximum age is:', maximum_age

    print 'The sorted list of ages is:', sorted_list

    print 'The average of the ages is:', average_age

    print 'The original input list of ages are:', ages

def AskForAges():

    age_list = []
    input = True

    while input == True:
        age_input = raw_input("What are the ages of people in your family. Please enter quit to exit: ")
        if age_input == "quit":
            input = False
        else:
            try:
                age = int(age_input)
                age_list.append(age)
            except ValueError:
                print "you have not entered an age integer value."

    return age_list

def GetManuipulateAndPrintAges():

    ages = AskForAges()
    minimum_age = Minimum(ages)
    maximum_age = Maximum(ages)
    average_age = CalculateAverage(ages)
    #appended_list = AppendToList(ages, [minimum_age + 10, maximum_age + 15])
    sorted_list = SortList(ages)
    PrintResults(ages, minimum_age, maximum_age, average_age, sorted_list)

GetManuipulateAndPrintAges()
                            
