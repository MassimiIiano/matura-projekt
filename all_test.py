import unittest
from src.classes.code_reader import create_mensa_file
from src.notifyer.main import *
import os

class Test(unittest.TestCase):
    # Variables for testing
    student1 = Student(123, "Massimo", "Cicchetti", "5IA", [1,2,3,4], "banana@banana.com")
    students = import_students(os.environ.get('PATH_MENSA'))
    students_today = get_students_today(students)

    @classmethod
    def setUpClass(cls):
        create_mensa_file()

    # ---------------------------------------------------------------- 
    # Notyfier
    # ----------------------------------------------------------------
    def test_get_absences(self):
        try:
            get_absences(self.students)
        except Exception:
            self.fail("Unexpected exception")
        pass


    def test_get_mensa_list(self):
        x = get_mensa_list()
        self.assertTrue(isinstance(x, list)) 


    def test_check_absences(self):
        ab = get_absences(self.students_today)
        pr = get_presences(self.students_today)

        stu =  ab + pr

        for s in self.students_today:
            if not s in stu:
                self.fail("not all elements presett in array")


    def test_get_undefined(self):
        self.assertEqual(get_undefined([self.student1], ['banana ananas']), ['banana ananas'])
        self.assertEqual(get_undefined([self.student1], ['Massimo Cicchetti']), [])

    # ---------------------------------------------------------------- 
    # Student
    # ----------------------------------------------------------------
    def test_get_students_today(self):
        try:
            get_students_today(self.students)
        except Exception:
            self.fail("Unexpected exception")

    def test_gen_qrcode(self):
        for student in self.students_today:
            student.gen_qrcode()


if __name__ == '__main__':
    unittest.main()