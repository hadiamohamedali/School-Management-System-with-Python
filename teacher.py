def writeTeacher():
    with open('TeacherPy.txt' , 'a') as file:
        c = 'y'
        while c == 'y':
            id = input('Enter The Teacher ID : ')
            name = input('Enter The Teacher Name : ')
            age = input('Enter The Teacher Age : ')
            subject = input('Enter The Subject : ')
            file.write(id + '\t' + name + '\t' + age + '\t' + subject + '\n')
            c = input ('Do You Want to Add Record Again (y / n)??')
        print('...File Saved Successfully...')

def readTeacher():
    with open('TeacherPy.txt' , 'r') as file:
        print('ID\tName\tAge\tSubject')
        print('-----------------------------------')
        for line in file:
            print(line , end = '')

def searchTeacher():
    id = input('Enter The ID of The Student to Search for : ')
    with open('TeacherPy.txt' , 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == id:
                found = True
                print('ID\tName\tAge\tSubject')
                print('-------------------------------------')
                print(line)
        if not found:
            print('...Teacher Not Found...')

def deleteTeacher():
    import os
    id = input('Enter The ID of Teacher to delete : ')
    file = open('TeacherPy.txt' ,'r')
    tempFile = open('TempTeacherPy.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
            found = True
        else:
            tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('TeacherPy.txt')
    os.rename('TempTeacherPy.txt' , 'Teacher.txt')
    if not found:
        print('...Teacher Not Found...')
    else:
        print('...Teacher Deleted Successfully...')

def updateTeacher():
    import os
    id = input('Enter The ID of Teacher to update : ')
    file = open('TeacherPy.txt' ,'r')
    tempFile = open('TempTeacherPy.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
            found = True
            age = input('Enter The New Age for this Teacher : ')
            line = fields[0] + '\t' + fields[1] + '\t' + age + '\t'+ fields[2]
        tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('TeacherPy.txt')
    os.rename('TempTeacherPy.txt' , 'Teacher.txt')
    if not found:
        print('...Teacher Not Found...')
    else:
        print('...Teacher Updated Successfully...')
   
    
        
    
