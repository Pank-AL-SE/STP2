import unittest
from converter_10p import Conver_10_P

class TestConver_10_P(unittest.TestCase):
    def test_int_to_char(self):
        self.assertEqual(Conver_10_P.int_to_char(10), "A")
        self.assertEqual(Conver_10_P.int_to_char(15), "F")
        self.assertEqual(Conver_10_P.int_to_char(0), "0")
        self.assertEqual(Conver_10_P.int_to_char(9), "9")
        self.assertEqual(Conver_10_P.int_to_char(11), "B")
        self.assertEqual(Conver_10_P.int_to_char(12), "C")
        self.assertEqual(Conver_10_P.int_to_char(13), "D")
        self.assertEqual(Conver_10_P.int_to_char(14), "E")

    def test_int_to_p(self):
        self.assertEqual(Conver_10_P.int_to_p(161, 16), "A1")
        self.assertEqual(Conver_10_P.int_to_p(10, 2), "1010")
        self.assertEqual(Conver_10_P.int_to_p(0, 16), "0")
        self.assertEqual(Conver_10_P.int_to_p(255, 16), "FF")
        self.assertEqual(Conver_10_P.int_to_p(1024, 16), "400")
        self.assertEqual(Conver_10_P.int_to_p(123, 8), "173")
        self.assertEqual(Conver_10_P.int_to_p(42, 2), "101010")
        self.assertEqual(Conver_10_P.int_to_p(100, 10), "100")

    def test_flt_to_p(self):
        self.assertEqual(Conver_10_P.flt_to_p(0.9375, 2, 4), "1111")
        self.assertEqual(Conver_10_P.flt_to_p(0.5, 16, 3), "800")
        self.assertEqual(Conver_10_P.flt_to_p(0.0, 2, 4), "")
        self.assertEqual(Conver_10_P.flt_to_p(0.625, 2, 4), "1010")
        self.assertEqual(Conver_10_P.flt_to_p(0.1, 16, 3), "199")
        self.assertEqual(Conver_10_P.flt_to_p(0.999, 16, 3), "FFB")
        self.assertEqual(Conver_10_P.flt_to_p(0.123, 8, 4), "0767")
        self.assertEqual(Conver_10_P.flt_to_p(0.75, 2, 4), "1100")

    def test_do(self):
        self.assertEqual(Conver_10_P.do(-17.875, 16, 3), "-11.E00")
        self.assertEqual(Conver_10_P.do(0.9375, 2, 4), "0.1111")
        self.assertEqual(Conver_10_P.do(0.0, 16, 3), "0")
        self.assertEqual(Conver_10_P.do(255.99609375, 16, 8), "FF.FF000000")
        self.assertEqual(Conver_10_P.do(123.456, 8, 4), "173.3513")
        self.assertEqual(Conver_10_P.do(-123.456, 8, 4), "-173.3513")
        self.assertEqual(Conver_10_P.do(1024.0, 16, 3), "400")
        self.assertEqual(Conver_10_P.do(0.1, 2, 8), "0.00011001")
        self.assertEqual(Conver_10_P.do(0.999, 16, 3), "0.FFB")
        self.assertEqual(Conver_10_P.do(42.42, 2, 8), "101010.01101011")

if __name__ == "__main__":
    unittest.main()