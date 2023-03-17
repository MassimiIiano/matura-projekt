import os
import sys
import tkinter as tk

sys.path.append(os.getenv('ROOT'))

from logic.reader.reader import repeat_function, write_to_file, create_mensa_file
from logic.fetch.fetch import get_student_by_name, import_students


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

def log_student(event=None, text_field=None, search_input=None):
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

def show_pdf():
    # open the pdf file saved in the env file
    os.system(f"start {os.getenv('PDF_PATH')}")


def main():
    # creates necessary folders and files
    setup()

    # starts gui
    root = tk.Tk()

    search_frame = tk.Frame(root)
    search_frame.pack(side="top", fill="x")

    search_input = tk.Entry(search_frame)
    search_input.pack(side="left", fill="x", expand=True)
    search_input.bind("<Return>", log_student)  # bind <Return> event to log_student function

    search_button = tk.Button(search_frame, text="Search", command=lambda: log_student(None, text_field, search_input))
    search_button.pack(side="right")

    text_field = tk.Text(root)
    text_field.pack(side="top", fill="both", expand=True)

    # add button to show PDF
    show_pdf_button = tk.Button(root, text="Mostra Carte", command=show_pdf, width=10)
    show_pdf_button.pack(side="left", padx=5, pady=5, fill="x")

    # add button to send emails
    send_emails_button = tk.Button(root, text="Manda Email", command=send_emails, width=10)
    send_emails_button.pack(side="right", padx=5, pady=5, fill="x")

    root.mainloop()

def show_pdf():
    # open the pdf file saved in the env file
    os.system(f"start {os.getenv('PDF_PATH')}")
    
def send_emails():
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    main()