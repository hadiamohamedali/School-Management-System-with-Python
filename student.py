def writeStudent():
    with open('StudentPy.txt' , 'a') as file:
        c = 'y'
        while c == 'y':
             id = input('Enter The Student ID : ')
             name = input('Enter The Student Name : ')
             age = input('Enter The Student Age : ')
             file.write(id + '\t' + name + '\t' + age + '\n')
             c = input('Do You Want To Add Record Again (y / n)??')
        print('...File Saved Successfully...')

def readStudent():
    with open('StudentPy.txt' , 'r') as file:
        print('ID\tName\tAge')
        print('-----------------------')
        for line in file:
            print(line , end = '')

def searchStudent():
    id = input('Enter The ID of The Student to search for : ')
    with open('StudentPy.txt' , 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == id:
                 found = True
                 print('ID\tName\tAge')
                 print('-------------------------------')
                 print(line)
        if not found:
            print('...Student Not Found...')

def deleteStudent():
    import os
    id = input('Enter The ID of Student to delete : ')
    file = open('StudentPy.txt' , 'r')
    tempFile = open('TempStudentPy.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
           found = True
        else:
            tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('StudentPy.txt')
    os.rename('TempStudentPy.txt' , 'StudentPy.txt')
    if not found:
        print('...Student Not Found...')
    else:
        print('...Student Deleted Successfully...')

def updateStudent():
    import os
    id = input('Enter The ID of Student to update : ')
    file = open('StudentPy.txt' , 'r')
    tempFile = open('TempStudentPy.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
           found = True
           age = input('Enter The New Age for this Student : ')
           line = fields[0] + '\t' + fields[1] + '\t' + age
        tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('StudentPy.txt')
    os.rename('TempStudentPy.txt' , 'StudentPy.txt')
    if found:
        print('...Student Updated Successfully...')
    else:
        print('...Student Not Found...')
    
     
