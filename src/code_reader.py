from datetime import datetime
import os
import time
import threading
from student import Student


class Reader():
    active = False

    def __init__(self, store: str, students: list[Student]):
        self.storeto = store
        # self.students = students

    def start(self):
        """Starts reading qrcodes form videostream"""
        self.active = True

        while self.active:
            data = input("studente: ")

            # exit if exit is endterd stop loop
            if data == "exit":
                self.active = False
                break

            # write log to file
            write_to_file(self.storeto, data)
            
            # std = find_student(data, self.students)
            
            # if std:
            #     print(std)
            # else:
            #     print("Studente non trovato")


def write_to_file(path, data):
    """Writes text data to a file"""
    with open(path, 'a') as f:
        f.write(data + '\n')
        f.close()

def create_mensa_file():
    # generate filename
    now = datetime.now()
    file_path = 'data/mensa/mensa' + now.strftime('%d-%m-%Y') + '.csv'

    # create file if not exists
    try:
        with open(file_path, 'x') as f:
            f.close()
    except FileExistsError:
        pass

    # set path to env
    os.environ["PATH_ATTENDANCES"] = os.path.abspath(file_path)


def repeat_function(func: callable, timeout: int = 60, exe: bool = True):
    # ensure that the function is called every minute
    def wrapper():
        while True:
            func()
            time.sleep(timeout)

    # execute the function once
    if exe:
        func()
    
    # creates and starts a daemon thread
    t = threading.Thread(
        target=wrapper, 
        daemon=True
    )

    t.start()

# TODO: (Opitonal) find student and assure the person that is using the program that everything is ok
def find_student(name: str, students: list[Student]) -> Student:

    # find student 
    for student in students:
        if name == student.name + student.surname:
            return student

    return None