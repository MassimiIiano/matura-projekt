# from barcode import Code128
# from barcode.writer import ImageWriter
import pandas as pd
import re
import os
from datetime import date
import qrcode

class Student:
    def __init__(self, id: str, name: str, surname: str, classe: str, presences: list[int], emails: list[str]):
        self.id = id
        self.name = name
        self.surname = surname
        self.classe = classe
        self.emails = emails
        self.presences = presences
        self.qr_path: str = os.environ.get('QR_PATH')

    def gen_qrcode(self):
        # create directory for qrcode if it doesn't exist
        if not os.path.exists(self.qr_path):
            os.makedirs(self.qr_path)
        
        # create qrcode file
        img = qrcode.make(self.name + " " + self.surname)
        img.save(self.qr_path + '/' + self.name + self.surname + ".png")

    
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.classe + " " + self.emails + " " + str(self.presences)


def import_students(path: str) -> list[Student]:
    """imports students from a csv file"""
    students = []

    # Read the data from the csv file
    data_mensa = pd.read_csv(path, sep=";")

    # Create a list of students from data
    for index, row in data_mensa.iterrows():
        # remove whitespace
        map(lambda x: x.strip(), row)

        # check days of mensa
        mensa_days = []
        days = [row['lun'], row['mar'], row['merc'], row['giov'], row['ven']]

        for i in range(len(days)):
            if days[i] == 'x':
                mensa_days.append(i)

        # check if emails are valid
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        student_emails = []
        emails = [row['mail madre'], row['mail padre']]

        for email in emails:
            if re.match(pat, str(email)):
                student_emails.append(email)

        # create student and append it to the list
        students.append(Student(row['N.'], row['Nome'], row['Cognome'], row['Classe'], mensa_days, student_emails))
    
    return students


def get_students_today(students: list[Student]) -> list[Student]:
    """returns the students that shoud go to mensa today"""
    res = []
    # loop over all students
    for student in students:
        # check if student should go to mensa today
        if date.today().weekday() in student.presences:
            res.append(student)

    return res