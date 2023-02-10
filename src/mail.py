import os
import smtplib
from email.mime.text import MIMEText
from .student import Student
from .get_data import get_absences, get_presences, get_undefined

# TODO shod work, but needs testing with paolo 
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

# TODO: implement
def send_report(present: list[Student], absent: list[Student], undef: list[str]) -> None:
    """Sends a Report of all absences and undefined people to the specified email address"""
    # variables that compose the text
    present = "Studenti presenti: \n"
    absent = "Studenti assenti: \n"
    undefined = "Studenti non identificati: \n"
    sep = "--- \n"

#     # check for presences
    for s in present:
        present += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

#     # check for absences
    for s in absent:
        absent += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

#     # check for undef people
    for name in undef:
        undefined += "- " + name + "\n"

    # TODO: send mails
    msg = absent + sep + undefined + sep + present

# TODO: implement 
def notify_parrent(student: Student) -> None:
    """Sends a Email in witch it informs about the absence of a student"""
    pass

def report():
    # TODO: finish whew you have acces to mail server
    # setnd report to personal
    send_report(get_presences(), get_absences(), get_undefined())

    # notify parents if student has missed mensa
    for student in get_absences():
        notify_parrent(student)
