import unittest
import os
from logic.import.get_data import import_students
from logic.student.student import Student

class Test(unittest.TestCase):
    # Variables for testing
    student1 = Student(123, "Massimo", "Cicchetti", "5IA", [1,2,3,4], "banana@banana.com")
    students = import_students(os.environ.get('PATH_MENSA'))

    def test_gen_qrcode(self):
        for student in self.students:
            student.gen_qrcode()


if __name__ == '__main__':
    unittest.main()