import re
binary = re.compile('^([01]{8})|([01]{16})$')
sample = '0001111000001111'
match = binary.match(sample)
if match:
    print('Match:', match.group())
else:
    print('No match found')

email = re.compile('[a-z]+@[a-z]+\.[a-z]+')
sample = 'E-Mail questions to bsmith@gmail.com before Thursday.'
match = email.search(sample)
if match:
    print('Start:', match.start())
    print('End:  ', match.end())
    print('Match:', match.group())
else:
    print('No match found')
