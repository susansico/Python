"""

Lab8Exercise2.py

"""

def UpdateList(list, element, new_element):

    if element in list:
        index = list.index(element)
        list[index] = new_element
    else:
        print element, "is not in list."

def RemoveListElement(list, element):

    if element in list:
        list.remove(element)
    else:
        print element, "is not in list."

def ConcatenateLists(list_1, list_2):

    return list_1 + list_2

def ManipulateLists():

    list_1 = [1, 3, 5, 7, 9, 11]
    list_2 = [2, 4, 6, 8, 10, 12]
    
    print "The first list is:", list_1
    print "The second list is:", list_2
    UpdateList(list_1, 9, 55)
    RemoveListElement(list_2, 10)
    concatenated_list = ConcatenateLists(list_1, list_2)
    print "The updated first list is:", list_1
    print "The second list with an item removed is:", list_2
    print "The concatenated list is:", concatenated_list

ManipulateLists()

    

    
