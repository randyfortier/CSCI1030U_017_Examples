grades = [71.5, 50.0, 48.5, 55.0, 64.5, 61.0, 100.0, 92.0]

def scaleAssignmentMark(percentage):
    return percentage * 0.15

#scaledGrades = map(scaleAssignmentMark, grades)
scaledGrades = map(lambda g: g * 0.15, grades)
#for grade in scaledGrades:
#    print(grade)
print('Scaled grades:', list(scaledGrades))

def min2(a, b):
    #return a if a < b else b    
    if a < b:
        return a 
    else:
        return b 

from functools import reduce
#minimum = reduce(min2, grades)
minimum = reduce(lambda a,b: a if a < b else b, grades)
print('The minimum grade is', minimum)

names = ['Frederick', 'Randy', 'Michael', 'Sally', 'Kenneth', 'Cynthia']
def isShortName(name):
    return len(name) < 7
    #if len(name) < 7:
    #    return True 
    #else:
    #    return False 
#shortNames = filter(isShortName, names)
shortNames = filter(lambda name: len(name) < 7, names)
print('The short names are:')
for name in shortNames:
    print(name)

print('---------------------------------------')

# syntax errors
age = 17
if age >= 18:  # remove the : to make a syntax error
    print('Vote!') # add a second closing bracket for another

# runtime errors 
courseName = 'CSCI 1030U'
#print('The 31st character in the string is', courseName[30])

# logic errors
name = 'Randy Fortier'
numRs = 0
for i in range(len(name)):
    #print('   checking', name[i])
    if name[i] == 'R' and name[i] == 'r':
        numRs += 1
print('The number of Rs in', name, 'is', numRs)

def printNTimes(n, message):
    if n <= 0:
        return
    print(message)
    printNTimes(n - 1, message)

printNTimes(5, 'Hello')
print('done')