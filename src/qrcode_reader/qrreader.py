from datetime import datetime
import cv2
import os
from src.classes import scedule


class QrcodeReader():
    active = False

    def __init__(self, vid, director, storeto):
        self.vid = vid
        self.director = director
        self.storeto = storeto

    def start(self):
        """Starts reading qrcodes form videostream"""
        self.active = True

        while self.active:
            # capture frame
            ret, frame = self.vid.read()
            data, bbox, straight_qrcode = self.director.directAndDecode(frame)

            if len(data) > 0:
                write_to_file(self.storeto, data)

    def stop(self):
        """Stops reading qrcodes form videostream"""
        self.active = False
        self.vid.release()


def write_to_file(path, data):
    """Writes text data to a file"""
    with open(path, 'a') as f:
        f.write(data + "\n")
        f.close()

def create_mensa_file():
    now = datetime.now()
    file_path = 'data/mensa/mensa' + now.strftime("%d-%m-%Y") + ".csv"
    with open(file_path, 'x') as f:
        f.close()

    os.environ["PATH_ATTENDANCES"] = os.path.abspath(file_path)

if __name__ == '__main__':

    scedule.schedule_as_thread(create_mensa_file())
    
    reader = QrcodeReader(
        cv2.VideoCapture(0), 
        cv2.QRCodeDetector(), 
        os.environ.get('PATH_ATTENDANCES')
    )

    reader.start()
