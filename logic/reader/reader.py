from datetime import datetime
import os
import time
import threading
from dotenv import load_dotenv
# load env variables
load_dotenv()

class Reader():
    active = False

    def __init__(self, store=False):
        self.storeto = store if store else create_mensa_file()

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
            
def accept(name: str):
    write_to_file(
        create_mensa_file(), 
        name
    )

def write_to_file(path, data):
    """Writes text data to a file"""
    with open(path, 'a') as f:
        f.write(data + '\n')
        f.close()

# TODO Test this function
def create_mensa_file():
    # generate filename
    now = datetime.now()
    # file_path = os.getenv('DATA') + os.getenv('LOGS') + now.strftime('%d-%m-%Y') + '.csv'
    file_path = os.getenv('DATA') + os.getenv('LOGS') + '/log' + now.strftime('%d-%m-%Y') + '.csv'

    # create file if not exists
    try:
        with open(file_path, 'x') as f:
            f.close()
    except FileExistsError:
        pass

    # set path to env
    return os.path.abspath(file_path)


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