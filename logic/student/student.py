import os
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageOps

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
        qr_content = self.name + " " + self.surname
        qr_image = qrcode.make(qr_content)
        qr_size = 200  # adjust the size of the QR code as needed
        
        # scale the QR code to the specified size
        qr_image = qr_image.resize((qr_size, qr_size))
        
        # create a white card image with the specified size
        card_width = 300  # adjust the width of the card as needed
        card_height = 400  # adjust the height of the card as needed
        padding = 20  # adjust the padding as needed
        card_image = Image.new('RGB', (card_width, card_height), color='white')
        
        # calculate the position to center the QR code and paste it onto the card
        qr_x = (card_width - qr_size) // 2
        qr_y = (card_height - qr_size - padding) // 2
        card_image.paste(qr_image, (qr_x, qr_y))
        
        # write the name and surname at the bottom of the card
        draw = ImageDraw.Draw(card_image)
        name_surname = self.name + " " + self.surname
        font = ImageFont.truetype("arial.ttf", 20)  # adjust the font and size as needed
        text_width, text_height = draw.textsize(name_surname, font=font)
        text_x = (card_width - text_width) // 2
        text_y = qr_y + qr_size + padding
        draw.text((text_x, text_y), name_surname, font=font, fill=(0, 0, 0))
        
        # save the image with a filename that includes the QR content
        filename = self.qr_path + '/' + self.name + self.surname + ".png"
        card_image.save(filename)
        
    
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.surname + " " + self.classe + " " + str(self.emails) + " " + str(self.presences)


