"""

Lab9Exercise.py

"""

def OpenFile(file_name, mode):

    try:
        file = open(file_name, mode)
    except IOError:
        file = False
        print "File can either not be created or found."

    return file

def WriteToFile(file_id, line):

    file_id.write(line)

def PrintFile(file_id, read_flag):

    if read_flag == 1:
        print file_id.read()
    elif read_flag == 2:
        print file_id.readline()
    elif read_flag == 3:
        print file_id.readlines()
    else:
        for line in file_id:
            print line

def GetNumberLinesInFile(file_id):

    file_list = []
    
    file_list = file_id.readlines()
        
    return len(file_list)

def CreateNewNumberedLinesFile(filename):

    new_file_list = []
    current_file_list = []

    file = OpenFile(filename, 'r')
    if file:
        current_file_list = file.readlines()
        for i, line in enumerate(current_file_list):
            new_file_list.append(str(i + 1) + '. ' + line)

        new_filename = filename.rsplit('.')[0] + '_numbered.' + filename.rsplit('.')[1]
        file.close()

        file = open(new_filename, 'w')
        for line in new_file_list:
            file.write(line + '\n')
        file.close()

        return new_filename

def FileManipulations():

    file_name_path = '/Users/Owner/Desktop/Python/Lab9Exercise.txt'

    #Exercise 1
    file = OpenFile(file_name_path, 'w')
    if file:
        WriteToFile(file, "Lab9Exercise.txt\n\n")
        file.close()
 
    file = OpenFile(file_name_path, 'a')
    if file:
        WriteToFile(file, "Progressive causes and candidates are winning.\n")
        WriteToFile(file, "Find Progressive causes candidates and get behind them.\n")
        WriteToFile(file, "What does it take to feel passion?\n")
        WriteToFile(file, "Activism?\n")
        file.close()

    #Exercise 2
    file = OpenFile(file_name_path, 'r')
    if file:
        PrintFile(file, 1)
        file.close()
    file = OpenFile(file_name_path, 'r')
    if file:
        PrintFile(file, 2)
        file.close()
    file = OpenFile(file_name_path, 'r')
    if file:
        PrintFile(file, 3)
        file.close()
    file = OpenFile(file_name_path, 'r')
    if file:
        PrintFile(file, 4)
        file.close()

    #Exercise 3
    file = OpenFile(file_name_path, 'r')
    if file:
        number_lines = GetNumberLinesInFile(file)
        print number_lines
    file.close()

   #Exercise 4 
    new_filename = CreateNewNumberedLinesFile(file_name_path)
    file = OpenFile(new_filename, 'r')
    if file:
        PrintFile(file, 4)
       
FileManipulations()
