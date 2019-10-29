class Course:
    #def __init__(self, code):
    #    self.code = code
    #    self.name = ''

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return self.name + ' (' + self.code + ')'

csci1030 = Course('CSCI 1030U', 'Introduction to Computer Science')
csci1030.code = 'COMP 1030U'
print(csci1030)
csci1060 = Course('CSCI 1060U', 'Programming Workshop I')
print(csci1060)

class PerfectSquares:
    def __init__(self):
        self.current = 0
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        self.current += 1
        return self.current ** 2

squares = PerfectSquares()
for value in squares:
    if (value < 1000):
        print(value)
    else:
        break

class Parakeet:
    def __init__(self, name, mass):
        self.name = name 
        self.mass = mass 
    
    def __lt__(self, other):
        if self.mass < other.mass:
            return True 
        else:
            return False

pete = Parakeet('Pete', 0.7)
lucy = Parakeet('Lucy', 0.6)
if pete < lucy:
    print('Pete has less mass than Lucy')
else:
    print('Lucy has less mass than Pete (or equal)')
