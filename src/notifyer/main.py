from datetime import datetime
from src.classes.mail import *
from src.classes.student import *
import os

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

def get_presences(list_sudents):
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


def report():
    # TODO: finish whew you have acces to mail server
    # setnd report to personal
    send_report(get_presences(), get_absences(), get_undefined())

    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)
