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
        self.qr_path: str = os.getenv('DATA') + os.getenv('QR')

    def gen_qrcode(self):
        """create qrcode file"""
        img = qrcode.make(self.name + " " + self.surname)
        img.save(self.qr_path + '/' + self.name + self.surname + ".png")
    
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.surname + " " + self.classe + " " + str(self.emails) + " " + str(self.presences)


