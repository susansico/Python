"""

Lab9HandlingFileErrorProcessing.py

"""

def PrintLinesInFile():

    try:
        file = open('/Users/Owner/Desktop/Python/example.txt')
    except IOError:
        print "File cannot be found."
    else:
        for line in file:
            print line

    file.close()

PrintLinesInFile()
