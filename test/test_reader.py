import os
import unittest
# TODO import logic.reader.reader is not recognized
import time
from logic.reader.reader import Reader, write_to_file, create_mensa_file, repeat_function

class TestReader(unittest.TestCase):
    def setUp(self):
        self.test_log_file = create_mensa_file()

    def tearDown(self):
        os.remove(self.test_log_file)

    def test_write_to_file(self):
        # Test that data is written to file
        data = "test data"
        write_to_file(self.test_log_file, data)
        with open(self.test_log_file, 'r') as f:
            contents = f.read()
        self.assertEqual(contents.strip(), data)

    def test_create_mensa_file(self):
        # Test that the mensa file is created
        file_path = create_mensa_file()
        self.assertTrue(os.path.exists(file_path))

    def test_repeat_function(self):
        # Test that the function is called repeatedly every 1 minute
        def test_func():
            test_func.called += 1
        test_func.called = 0
        repeat_function(test_func, timeout=1, exe=False)
        time.sleep(3)
        self.assertGreater(test_func.called, 1)

if __name__ == '__main__':
    unittest.main()