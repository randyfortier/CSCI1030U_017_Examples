sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midtermMarks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('grade_output.csv', 'w') as file:
    for i in range(len(sids)):
        sid = sids[i]
        mark = midtermMarks[i]
        file.write(sid + ',' + str(mark) + '\n')

import json
grades = {
    '100000001': 72.0,
    '100000002': 61.5,
    '100000003': 50.0,
    '100000004': 65.25,
    '100000005': 44.0,
    '100000006': 39.5,
    '100000007': 68.0
}
with open('midterm_marks.json', 'w') as file:
    json.dump(grades, file)

for num in [5,4,3,2,1,0]:
    try:
        print(1 / num)
    except ZeroDivisionError as error:
        print('infinity')

print('all done')

class TooYoungError(Exception):
    pass

def watchMatureShow(age):
    if age < 18:
        raise TooYoungError('You are too young to watch this show!')
    print('Winter is coming!')

age = int(input('How old are you? '))
try:
    watchMatureShow(age)
except TooYoungError as error:
    print('You cannot watch this show, sorry!')
