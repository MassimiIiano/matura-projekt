from student import *

def test_import_students():
    return import_students('data/Mensa classi prime.csv')

students = test_import_students()

students.append('banana')