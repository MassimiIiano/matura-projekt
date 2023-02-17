import unittest
import os
from mail import *

class TestSendEmail(unittest.TestCase):

    def test_send_email(self):
        """Check that the email was sent successfully"""
        to = 'recipient@example.com'
        subject = 'Test, this is the subject'
        content = 'This is a test email from Python.'

        os.environ['SENDER_EMAIL'] = 'alfieriblz@schools.fuss.bz.it'
        os.environ['SMTP_SERVER'] = '10.0.101.101'
        os.environ['SMTP_PORT'] = '25'

        send_email(to, content, subject)


if __name__ == '__main__':
    unittest.main()