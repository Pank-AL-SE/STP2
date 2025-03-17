import unittest
from converter_p10 import Conver_P_10

class TestConver_P_10(unittest.TestCase):
    def test_char_to_num(self):
        self.assertEqual(Conver_P_10.char_to_num('A'), 10)
        self.assertEqual(Conver_P_10.char_to_num('F'), 15)
        self.assertEqual(Conver_P_10.char_to_num('0'), 0)
        self.assertEqual(Conver_P_10.char_to_num('9'), 9)

    def test_dval(self):
        self.assertEqual(Conver_P_10.dval("A5.E", 16), 165.875)
        self.assertEqual(Conver_P_10.dval("101.11", 2), 5.75)
        self.assertEqual(Conver_P_10.dval("FF.FF", 16), 255.99609375)
        self.assertEqual(Conver_P_10.dval("0.1", 2), 0.5)

if __name__ == "__main__":
    unittest.main()