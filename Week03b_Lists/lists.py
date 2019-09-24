students = ['Carla', 'Robert', 'Dawn']
print('index: ', students[1])
print('slice1:', students[1:1])
name = 'abcdef'
print('slice2:', name[3:3])
str = 'Fred'
ageStr = '21'
age = int(ageStr)
#ageStr = str(age) # str overwritten

print('- ' * 20)

print('Graphics?')
rows = 5
cols = 80
for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print('')

print('More graphics?')
for r in range(rows):
    print(' ' * r + '*' * cols)

name = 'Albert Bowman'
for letter in name:
    print(letter, end=' ')
print('')

# coding exercise #1
sentence = 'the quick brown fox jumped over the lazy dog'
words = sentence.split(' ')
wordsReverse = []
for word in words:
    wordsReverse.insert(0, word)
reverseSentence = ' '.join(wordsReverse)
print(reverseSentence)

nums = [1,2,3,4,5]
if 7 in nums:
    index = nums.index(7)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
tensor = [matrix, matrix, matrix]
print(tensor)

# coding exercise #2
midtermMarks = [25.0, 75.0, 62.5, 74.25]
sum = 0
for mark in midtermMarks:
    sum += mark
print('Average:', sum / len(midtermMarks))