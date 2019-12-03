# Practice Exam - Question #1
def printContent(content):
    print(content)

def processHTML(filename, handleContent):
    # read in the file's contents
    with open(filename, 'r') as file:
        fileContents = file.read()

    # go through the contents one char at a time
    inContent = False 
    content = ''
    for character in fileContents:
        if inContent and character == '<':
            # finished the content
            handleContent(content)
            content = ''
            inContent = False 
        elif not inContent and character == '>':
            # starting the content
            inContent = True
        elif inContent:
            # add the character to our content
            content += character

def measureContent(content):
    print(len(content))

processHTML('sample.html', measureContent)

def multiplyMatrices(a, b):
    numOperations = 0
    n = len(a)

    # make an zero matrix
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        result.append(row)

    # multiply the matrices
    for r in range(n):
        for c in range(n):
            value = 0.0
            for i in range(n):
               # multiply the rth row, ith column in the first matrix with the ith row, cth column in the second
               value += a[r][i] * b[i][c]   # count only this line

               # we executed the line, so increase the count
               numOperations += 1
            result[r][c] = value;

    print('Number of operations:', numOperations)
    return result

n = 1000
'''
n    numOperations
---  -------------
1    1
2    8
10   1000
100  1000000
1000 
'''
a = []
for row in range(n):
    newRow = []
    for col in range(n):
        newRow.append(col)
    a.append(newRow)

b = []
for row in range(n):
    newRow = []
    for col in range(n):
        newRow.append(col)
    b.append(newRow)

#print('a =', a)
#print('b =', b)

result = multiplyMatrices(a, b)
#print(result)

# Practice Problem #10
def move1(source, dest):
    print("Move top ring from peg ", source, "to peg ", dest)

def solveHanoi(numRings, startingRing, endingRing, tempRing):
    if numRings == 0:
        return

    # move numRings - 1 rings from startingRing to tempRing
    solveHanoi(numRings - 1, startingRing, tempRing, endingRing)

    # move 1 ring from startingRing to endingRing
    move1(startingRing, endingRing)

    # move numRings - 1 from tempRing to endingRing
    solveHanoi(numRings - 1, tempRing, endingRing, startingRing)
