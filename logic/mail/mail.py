import os
import smtplib
from datetime import date
from email.mime.text import MIMEText
from logic.fetch.fetch import get_absences, get_presences, get_undefined
from logic.student.student import Student
from dotenv import load_dotenv
# load env variables
load_dotenv()

# TODO TEST ALLL FLUNCTIONS


def send_email(to: list[str], content: str, subject: str) -> None:
    sender = os.environ.get('SENDER_EMAIL')
    smtp_server = os.environ.get('SMTP_SERVER')
    
    message = MIMEText(content)
    message['to'] = ', '.join(to)
    message['from'] = sender
    message['subject'] = subject

    server = smtplib.SMTP(smtp_server, os.environ.get('SMTP_PORT'))
    server.sendmail(sender, to, message.as_string())
    server.quit()


def send_report(present: list[Student], absent: list[Student], undef: list[str]) -> None:
    """Sends a Report of all absences and undefined people to the specified email address"""
    # variables that compose the text
    present = "Studenti presenti: \n"
    absent = "Studenti assenti: \n"
    undefined = "Studenti non identificati dal sistema: \n"
    sep = "------------------------ \n"

    # check for presences
    for s in present:
        present += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

    # check for absences
    for s in absent:
        absent += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

    # check for undef people
    for name in undef:
        undefined += "- " + name + "\n"

    msg = absent + sep + undefined + sep + present
    
    send_email(os.getenv('RECEIVER_EMAIL'), msg, "Report Mensa")
    

def notify_parrent(student: Student) -> None:
    """Sends a Email in witch it informs about the absence of a student"""
    for parent in student.emails:
        send_email(parent, f"Lo/la studente/essa {student.name} {student.surname} e stata registrato/a come assente il {date.today()}", f"Assenza in Mensa il {date.today()}")
        

def report():
    # setnd report to personal
    send_report(get_presences(), get_absences(), get_undefined())

    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)

def notify():
    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)