from barcode import Code128
# from barcode.writer import ImageWriter
import pandas as pd
import numpy as np
from datetime import date

class Student:
    def __init__(self, id, name, surname, classe, presences, emails=[None, None]):
        self.id = id
        self.name = name
        self.surname = surname
        self.classe = classe
        self.emails = emails
        self.presences = presences

    def gen_barcode(self):
        my_code = Code128(self.name + " " + self.surname)
        my_code.save("barcodes/" + self.name + self.surname)

    def __str__(self):
        return self.name + " " + self.classe + " " + self.emails + " " + str(self.presences)


def get_students(path_data):
    students = []
    # Read the data from the csv file
    data_mensa = pd.read_csv(path_data, sep=";")

    # Create a list of students from data
    for index, row in data_mensa.iterrows():
        
        students.append(Student(row['N.'], row['Nome']), row['Cognome'], row['Classe'], row[''])
    
    return students

def get_students_today():
    res = []
    for student in get_students('data\Mensa classi prime.csv'):
        if date.today().weekday() in student.presences:
            res.append(student)
    return res