from datetime import datetime
import os
import time
import threading



class Reader():
    active = False

    def __init__(self, store: str):
        self.storeto = store

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