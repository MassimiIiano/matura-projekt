import unittest
import os
from src.classes.mail import *

class Test(unittest.TestCase):
    def test_send_mail(self):
        port = int(os.environ.get('MAIL_PORT'))
        server = str(os.environ.get('MAIL_SERVER'))
        sender = "alfieriblz@schools.fuss.bz.it"
        recivers = ['massimiliano.mola.bzs@gmail.com']
        msg = """From: Fuss <alfieriblz@schools.fuss.bz.it>
To: Massimiliano <massimiliano.mola.bzs@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""


        send_mail(port, server, sender, recivers, msg)


if __name__ == '__main__':
    unittest.main()