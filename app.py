import os
import sys
import tkinter as tk
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image
from fpdf import FPDF

sys.path.append(os.getenv('ROOT'))

from logic.reader.reader import repeat_function, write_to_file, create_mensa_file
from logic.fetch.fetch import get_student_by_name, import_students


def setup():
    # create folders to store data
    paths = [
        os.getenv('DATA') + os.getenv('LOGS', '/logs'),
        os.getenv('DATA') + os.getenv('QR', '/qrcodes'),
        os.getenv('DATA') + os.getenv('PDF', '/pdf'),
    ]
    
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    
    # generate qrcodes
    for student in import_students(os.getenv('DATA') + os.getenv('STUDENTS')):
        student.gen_qrcode()
    
    # create cards as pdf files
    # ---------------------------------
    # Directory containing PNG images
    image_directory = os.getenv('DATA') + os.getenv('QR')

    # Get list of PNG files in directory
    png_files: list[str] = [image_directory + '/' + f for f in os.listdir(image_directory) if f.endswith('.png')]

    # Create PDF document
    pdf_file: str = os.getenv('DATA') + os.getenv('PDF', '/pdf') + "/cards.pdf"


    convert_to_pdf(png_files, pdf_file)
    
    # Create a file to store the log of the day
    # creates new file every day
    repeat_function(create_mensa_file, exe=True)
    
def convert_to_pdf(png_files: list[str], pdf_file: str):
    # Define the dimensions and margins of a card
    w, h = 85.60, 53.98  # mm
    
    # Define the dimensions of the A4 paper
    page_w, page_h = 210, 297  # mm
    
    # Create a new PDF document
    pdf = FPDF()
    
    # Iterate over the PNG files and add them to the PDF
    x, y = 0, 0
    for image in png_files:
        # Check if there is enough space to add the image to the current page
        if x + w <= page_w and y + h <= page_h:
            # Add the image to the current page
            pdf.add_page()
            pdf.image(image, x, y, w, h)
            x += w
        else:
            # There is no more space on the current page, start a new page
            x = 0
            y += h
            if y + h > page_h:
                # There is no more space on the current page, start a new page
                pdf.add_page()
                x, y = 0, 0
            pdf.image(image, x, y, w, h)
            x += w
            
    # Save the PDF document
    pdf.output(pdf_file, "F")


def log_student(event=None):
    name = search_input.get()  # get the name from the input field
    student = get_student_by_name(name)  # search for the student with the matching name
    if student:
        # display the student info in the text field
        # text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, f"Studente identificato: " + str(student))
    else:
        # text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, f"Studente non identificato: '{name}'")
        
    # delete the name from the input field
    search_input.delete(0, tk.END)
    
    text_field.insert(tk.END, "\n")
    write_to_file(
        create_mensa_file(),
        name
    )
    # empty the input field
    search_input.delete(0, tk.END)



if __name__ == '__main__':
    # creates necessary folders and files
    setup()
    
    # starts gui
    root = tk.Tk()

    search_frame = tk.Frame(root)
    search_frame.pack(side="top", fill="x")

    search_input = tk.Entry(search_frame)
    search_input.pack(side="left", fill="x", expand=True)
    search_input.bind("<Return>", log_student)  # bind <Return> event to log_student function

    search_button = tk.Button(search_frame, text="Search", command=log_student)
    search_button.pack(side="right")

    text_field = tk.Text(root)
    text_field.pack(side="bottom", fill="both", expand=True)

    root.mainloop()