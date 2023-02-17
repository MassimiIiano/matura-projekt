from datetime import datetime
from datetime import date
import pandas as pd
import re
import os
from logic.student.student import Student

def get_mensa_list():
    """Returns an array of the names of the student that did go to the mensa doday"""
    res = []
    # open mensa file
    with open('data/mensa/mensa' + datetime.now().strftime("%d-%m-%Y") + ".csv", 'r') as f:
        lines = f.readlines()
        
    # clear name of students
    for l in lines:
        res.append(l.replace("\n", "").strip())
        
    # replace doubles
    return list(dict.fromkeys(res))

def get_presences(list_sudents: list[Student]):
    """returns all the students thad did go to the mensa"""
    attenddances = get_mensa_list()
    ret = []

    for s in list_sudents:
        if s.name + " " + s.surname in attenddances:
            ret.append(s)

    return ret

def get_absences(students):
    """returns all the students that were absent from the mensa"""
    return [x for x in students if x not in get_presences(students)]

def get_undefined(students, attenddancies) -> list[str]:
    """returns an array of the names of people that soud not have been in the mensa"""
    names = []
    for s in students:
        names.append(s.name + " " + s.surname)
    
    return [x for x in attenddancies if x not in names]


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

def get_all() -> list[Student]:
    return import_students(os.environ.get('PATH_MENSA'))

def get_students_today(students: list[Student]) -> list[Student]:
    """returns the students that shoud go to mensa today"""
    res = []
    # loop over all students
    for student in students:
        # check if student should go to mensa today
        if date.today().weekday() in student.presences:
            res.append(student)

    return res
