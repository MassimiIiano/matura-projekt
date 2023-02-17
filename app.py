import os
from logic.fetch.fetch import import_students
from logic.reader.reader import Reader, create_mensa_file, repeat_function

def setup():
    # create folders to store data
    paths = [
        os.getenv('DATA') + os.getenv('LOGS'),
        os.getenv('DATA') + os.getenv('QR'),
    ]
    
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    
    # generate qrcodes
    for student in import_students(os.getenv('DATA') + os.getenv('STUDENTS')):
        student.gen_qrcode()
    
    # Create a file to store the log of the day
    # creates new file every day
    repeat_function(create_mensa_file, exe=True)

if __name__ == '__main__':
    # creates necessary folders and files
    setup()
    
    # reads input
    reader = Reader()
    reader.start()


