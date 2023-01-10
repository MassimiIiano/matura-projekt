from src.classes.mail import *
from src.classes.student import *
import os

# TODO: all the functions AND TEST THEM
def get_mensa_list():
    """Returns an array of the names of the student that did go to the mensa doday"""
    res = []
    # open mensa file
    with open(os.getenv('PATH_MENSA'), 'r') as f:
        lines = f.readlines()
    # clear name of students
    for l in lines:
        res.append(l.replace("\n", "").strip())
    # replace doubles
    return list(dict.fromkeys(res))

def get_presences():
    """returns all the students thad did go to the mensa"""
    list_sudents = get_students_today()
    attenddances = get_mensa_list()
    ret = []

    for s in list_sudents:
        if s.name + " " + s.surname in attenddances:
            ret.append(s)

    return ret

def get_absences():
    """returns all the students that were absent from the mensa"""
    pass

def get_undefined():
    """returns an array of the names of people that soud not have been in the mensa"""
    students = get_students_today()
    attenddances = get_mensa_list()
    names = []
    for s in students:
        names.append(s.name + " " + s.surname)

# TODO: check if it works
    return list(set(attenddances) - set(names))

if __name__ == "__main__":
    # setnd report to personal
    send_report(os.getenv("REPORT_TO"), get_presences(), get_absences(), get_undefined())

    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)
