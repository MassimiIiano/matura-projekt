from datetime import datetime
import os
from src.classes.scedule import schedule_as_thread


class Reader():
    active = False

    def __init__(self, storeto):
        self.storeto = storeto

    def start(self):
        """Starts reading qrcodes form videostream"""
        self.active = True

        while self.active:
            data = input("studente: ")
            write_to_file(self.storeto, data)

    def stop(self):
        """Stops reading qrcodes form videostream"""
        self.active = False
        self.vid.release()


def write_to_file(path, data):
    """Writes text data to a file"""
    with open(path, 'a') as f:
        f.write(data)
        f.close()

def create_mensa_file():
    now = datetime.now()
    file_path = 'data/mensa/mensa' + now.strftime("%d-%m-%Y") + ".csv"
    with open(file_path, 'x') as f:
        f.close()

    os.environ["PATH_ATTENDANCES"] = os.path.abspath(file_path)

if __name__ == '__main__':

    schedule_as_thread(create_mensa_file())
    
    reader = Reader(
        os.environ.get('PATH_ATTENDANCES')
    )

    reader.start()