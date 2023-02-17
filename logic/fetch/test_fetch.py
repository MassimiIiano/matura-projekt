import os
import unittest
from datetime import datetime
from logic.fetch.fetch import get_mensa_list, get_presences, get_absences, get_undefined, import_students, get_students_today
from logic.student.student import Student

class TestFetch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # create a test CSV file
        cls.test_file_path = "data/mensa/test.csv"
        with open(cls.test_file_path, "w") as f:
            f.write("N.;Nome;Cognome;Classe;lun;mar;merc;giov;ven;mail madre;mail padre\n")
            f.write("1;Alice;Rossi;1A;x;;x;x;x;alice.rossi@example.com;\n")
            f.write("2;Bob;Verdi;1B;x;x;;x;;bob.verdi@example.com;\n")
            f.write("3;Charlie;Neri;1A;x;x;x;x;x;charlie.neri@example.com;charlie.neri@example.com\n")
        
    @classmethod
    def tearDownClass(cls):
        # delete the test CSV file
        os.remove(cls.test_file_path)

    def test_get_mensa_list(self):
        # create a test mensa file
        with open('data/mensa/mensa' + datetime.now().strftime("%d-%m-%Y") + ".csv", 'w') as f:
            f.write("Alice Rossi\n")
            f.write("Charlie Neri\n")

        expected = ["Alice Rossi", "Charlie Neri"]
        actual = get_mensa_list()
        self.assertEqual(expected, actual)

    def test_get_presences(self):
        students = [
            Student("1", "Alice", "Rossi", "1A", [0, 2, 3, 4], ["alice.rossi@example.com"]),
            Student("2", "Bob", "Verdi", "1B", [0, 1, 3], ["bob.verdi@example.com"]),
            Student("3", "Charlie", "Neri", "1A", [0, 1, 2, 3, 4], ["charlie.neri@example.com", "charlie.neri@example.com"])
        ]
        expected = [students[0], students[2]]
        actual = get_presences(students)
        self.assertEqual(expected, actual)

    def test_get_absences(self):
        students = [
            Student("1", "Alice", "Rossi", "1A", [0, 2, 3, 4], ["alice.rossi@example.com"]),
            Student("2", "Bob", "Verdi", "1B", [0, 1, 3], ["bob.verdi@example.com"]),
            Student("3", "Charlie", "Neri", "1A", [0, 1, 2, 3, 4], ["charlie.neri@example.com", "charlie.neri@example.com"])
        ]
        expected = [students[1]]
        actual = get_absences(students)
        self.assertEqual(expected, actual)