import unittest
from control import Control

class TestControl(unittest.TestCase):
    def setUp(self):
        self.control = Control()

    def test_do_command(self):
        self.assertEqual(self.control.do_command(5), "5")
        self.assertEqual(self.control.do_command(16), "5.")
        self.assertEqual(self.control.do_command(17), "5")
        self.assertEqual(self.control.do_command(18), "")

        self.control.do_command(5)
        self.control.do_command(16)
        self.control.do_command(5)
        result = self.control.do_command(19)
        self.assertEqual(result, "5.800")

if __name__ == "__main__":
    unittest.main()