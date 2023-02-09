# TODO: check that functions work properly

import os
import smtplib
from email.mime.text import MIMEText

def send_email(to, content, subject):
    sender = os.environ.get('SENDER_EMAIL')
    smtp_server = os.environ.get('SMTP_SERVER')
    
    message = MIMEText(content)
    message['to'] = ', '.join(to)
    message['from'] = sender
    message['subject'] = subject

    server = smtplib.SMTP(smtp_server, os.environ.get('SMTP_PORT'))
    server.sendmail(sender, to, message.as_string())
    server.quit()





def send_report(sender_email, reciver_emails, present, absent, undef):
    """Sends a Report of all absences and undefined people to the specified email address"""
    # variables that compose the text
    present = "Studenti presenti: \n"
    absent = "Studenti assenti: \n"
    undefined = "Studenti non identificati: \n"
    separator = "--- \n"

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
    msg = absent + separator + undefined + separator + present

# TODO: check if it works
def notify_parrent(student, sender):
    """Sends a Email in witch it informs about the absence of a student"""
    for email in student.get_emails():
        send_mail(sender, email, "La iformiamo che suo figlio/a ...")
    pass

# # TODO: dosn't work properly
# def get_absences():
#     return [x for x in get_students_today() if x not in get_presences()]
