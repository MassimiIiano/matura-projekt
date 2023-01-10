
def send_mail():
    """Sends a Email to the specified email address"""
    pass

def send_report():
    """Sends a Report of all absences and undefined people to the specified email address"""
    pass

def notify_parrent(student):
    """Sends a Email in witch it informs about the absence of a student"""
    pass

# def get_attenddances():
#     res = []
#     with open('data/attendances.csv', 'r') as f:
#         lines = f.readlines()
#     for l in lines:
#         res.append(l.replace("\n", "").strip())
#     return list(dict.fromkeys(res))


# def create_report(studens_present):
#     present = "Studenti presenti: \n"
#     absent = "Studenti assenti: \n"
#     undefined = "Studenti non identificati: \n"
#     separatore = "--- \n"

#     # check for presences
#     for s in get_presences():
#         present += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

#     # check for absences
#     for s in get_absences():
#         absent += "- " + s.name + " " + s.surname + " " + s.classe + "\n"

#     # check for undef people
#     for name in get_undef():
#         undefined += "- " + name + "\n"

#     return absent + separatore + undefined + separatore + present

# def get_presences():
#     list_sudents = get_students_today()
#     attenddances = get_attenddances()
#     ret = []

#     for s in list_sudents:
#         if s.name + " " + s.surname in attenddances:
#             ret.append(s)

#     return ret

# # TODO: dosn't work properly
# def get_absences():
#     return [x for x in get_students_today() if x not in get_presences()]

# def get_undef():
#     students = get_students_today()
#     attenddances = get_attenddances()
#     names = []
#     for s in students:
#         names.append(s.name + " " + s.surname)

#     return list(set(attenddances) - set(names))

# print(create_report(get_students('data/test_mensa.csv', 'data/test_contact.csv')))
