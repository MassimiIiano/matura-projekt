import os
import unittest
from logic.student.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.test_student = Student("123", "John", "Doe", "9A", [1, 1, 0], ["john.doe@example.com"])

    def test_gen_qrcode(self):
        # Test that a QR code image file is generated
        self.test_student.gen_qrcode()
        qr_code_path = os.getenv('DATA') + os.getenv('QR') + '/JohnDoe.png'
        self.assertTrue(os.path.isfile(qr_code_path))

    def test_get_emails(self):
        # Test that the correct email addresses are returned
        expected_emails = ["john.doe@example.com"]
        self.assertEqual(self.test_student.get_emails(), expected_emails)

    def test_str(self):
        # Test that the __str__ method returns the expected string representation
        expected_str = "John Doe 9A ['john.doe@example.com'] [1, 1, 0]"
        self.assertEqual(str(self.test_student), expected_str)

if __name__ == '__main__':
    unittest.main()