from src.classes.mail import *
from src.classes.student import *
import os

# TODO: all the functions 
def get_mensa_list():
    """Returns an array of the names of the student that did go to the mensa doday"""
    pass

def get_presences():
    """returns all the students thad did go to the mensa"""
    pass

def get_absences():
    """returns all the students that were absent from the mensa"""
    pass

def get_undefined():
    """returns an array of the names of people that soud not have been in the mensa"""
    pass

if __name__ == "__main__":
    # setnd report to personal
    send_report(os.getenv("REPORT_TO"), get_presences(), get_absences(), get_undefined())

    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)
