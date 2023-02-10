
import os
import qrcode

class Student:
    def __init__(self, id: str, name: str, surname: str, classe: str, presences: list[int], emails: list[str]):
        self.id = id
        self.name = name
        self.surname = surname
        self.classe = classe
        self.emails = emails
        self.presences = presences
        self.qr_path: str = os.environ.get('QR_PATH')

    def gen_qrcode(self):
        # create directory for qrcode if it doesn't exist
        if not os.path.exists(self.qr_path):
            os.makedirs(self.qr_path)
        
        # create qrcode file
        img = qrcode.make(self.name + " " + self.surname)
        img.save(self.qr_path + '/' + self.name + self.surname + ".png")

    
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.classe + " " + self.emails + " " + str(self.presences)


