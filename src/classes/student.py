# from barcode import Code128
# from barcode.writer import ImageWriter
import pandas as pd
import re
from datetime import date
import qrcode

class Student:
    def __init__(self, id, name, surname, classe, presences, emails):
        self.id = id
        self.name = name
        self.surname = surname
        self.classe = classe
        self.emails = emails
        self.presences = presences


    # def gen_barcode(self):
    #     my_code = Code128(self.name + " " + self.surname)
    #     my_code.save("barcodes/" + self.name + self.surname)


    def gen_qrcode(self):
        img = qrcode.make(self.name + " " + self.surname)
        img.save("qrcodes/" + self.name + self.surname + ".png")

    
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.classe + " " + self.emails + " " + str(self.presences)


def import_students(path_data):
    """imports students from a csv file"""
    students = []
    # Read the data from the csv file
    data_mensa = pd.read_csv(path_data, sep=";")

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


def get_students_today(student_list=[]):
    """returns the students that shoud go to mensa today"""
    res = []
    for student in student_list:
        if date.today().weekday() in student.presences:
            res.append(student)
    return res