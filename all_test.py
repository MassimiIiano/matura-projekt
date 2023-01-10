import unittest
from src.notifyer.main import *
import os

class Test(unittest.TestCase):
    # Variables for testing
    students = import_students(os.environ.get('PATH_MENSA'))
    students_today = get_students_today(import_students(os.environ.get('PATH_MENSA')))
    # ---------------------------------------------------------------- 
    # Global
    # ----------------------------------------------------------------
    def test_env_variables(self):
        self.assertEqual(os.environ.get('PATH_MENSA'), "C:/Users/massi/Documents/School/5IA/projekt_matura/data/Mensa classi prime.csv")


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

    # ---------------------------------------------------------------- 
    # Student
    # ----------------------------------------------------------------
    def test_get_students_today(self):
        try:
            get_students_today(self.students)
        except Exception:
            self.fail("Unexpected exception")


        


if __name__ == '__main__':
    unittest.main()
