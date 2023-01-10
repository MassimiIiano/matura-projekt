import smtplib, ssl
from src.classes.student import Student

# TODO: check that functions work properly

def send_mail(sender_email, reciver_email, message):
    """Sends a Email to the specified email address"""
    port = 465  # For SSL
    password = input("Type your password and press enter: ")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("massimiliano.mola.bzs@gmail.com", password)
        # TODO: send email  
        # server.sendmail(sender_email, receiver_email, message)


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
