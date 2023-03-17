import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

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
        # Set dimensions for the output image
        card_size = (600, 375)  # width, height
        qr_size = 250  # width and height of the QR code
        text_height = 60  # height of the text below the QR code
        space = 20  # extra space between the QR code and the text
        
        # Create a new image with white background
        canvas = Image.new("RGB", card_size, color="white")
        
        # Create QR code image
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=2)
        qr.add_data(f"{self.name} {self.surname}")
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Calculate position of the QR code on the canvas
        qr_pos = ((card_size[0]-qr_size)//2, (card_size[1]-qr_size-text_height-space)//2)
        
        # Resize the QR code to a fixed size and paste it onto the canvas
        qr_image = qr_image.resize((qr_size, qr_size))
        canvas.paste(qr_image, qr_pos)
        
        # Add name and surname below the QR code
        draw = ImageDraw.Draw(canvas)
        name_pos = (card_size[0]//2, qr_pos[1]+qr_size+space)
        font = ImageFont.truetype("arial.ttf", size=20)
        draw.text(name_pos, f"{self.name} {self.surname}", font=font, fill="black", anchor="ms")
        
        # Save image to file
        image_path = os.path.join(self.qr_path, f"{self.name}{self.surname}.png")
        canvas.save(image_path)
        
    def get_emails(self):
        return self.emails


    def __str__(self):
        return self.name + " " + self.surname + " " + self.classe + " " + str(self.emails) + " " + str(self.presences)


