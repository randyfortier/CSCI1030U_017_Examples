class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest 

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.carla = Student(4.0, 'Carla Rodriguez')

    def test_set_mark(self):
        self.carla.set_mark('CSCI 1030U', 75.0)
        self.assertEqual(len(self.carla.marks), 1)
        self.assertEqual(self.carla.marks[0], 75.0)

    def test_get_average(self):
        self.carla.set_mark('CSCI 1030U', 70.0)
        self.carla.set_mark('CSCI 1060U', 60.0)
        self.carla.set_mark('MATH 1010U', 80.0)
        self.assertEqual(self.carla.get_average(), 70.0)

unittest.main()  # execute the tests