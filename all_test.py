import unittest
from src.notifyer.main import *
import os

class Test(unittest.TestCase):
    students = import_students(os.environ.get('PATH_MENSA'))

    def test_get_students_today(self):
        try:
            get_students_today(self.students)
        except Exception:
            self.fail("Unexpected exception")

    def test_get_absences(self):
        try:
            get_absences(self.students)
        except Exception:
            self.fail("Unexpected exception")
        pass

    def test_env_variables(self):
        self.assertEqual(os.environ.get('PATH_MENSA'), "C:/Users/massi/Documents/School/5IA/projekt_matura/data/Mensa classi prime.csv")

    def test_get_mensa_list(self):
        x = get_mensa_list()
        self.assertTrue(isinstance(x, list)) 
        

if __name__ == '__main__':
    unittest.main()