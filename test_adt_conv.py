import unittest
from adt_conver_p import ADTConver10P

class TestADTConver10P(unittest.TestCase):

    def test_int_to_Char(self):
        self.assertEqual(ADTConver10P._int_to_Char(0), '0')
        self.assertEqual(ADTConver10P._int_to_Char(9), '9')
        self.assertEqual(ADTConver10P._int_to_Char(10), 'A')
        self.assertEqual(ADTConver10P._int_to_Char(35), 'Z')
        with self.assertRaises(ValueError):
            ADTConver10P._int_to_Char(36)
        with self.assertRaises(ValueError):
            ADTConver10P._int_to_Char(-1)

    def test_int_to_P(self):
        self.assertEqual(ADTConver10P._int_to_P(10, 2), '1010')
        self.assertEqual(ADTConver10P._int_to_P(255, 16), 'FF')
        self.assertEqual(ADTConver10P._int_to_P(-255, 16), '-FF')
        self.assertEqual(ADTConver10P._int_to_P(0, 8), '0')

    def test_flt_to_P(self):
        self.assertEqual(ADTConver10P._flt_to_P(0.5, 2, 4), '1000')
        self.assertEqual(ADTConver10P._flt_to_P(0.999, 16, 2), 'FF')
        self.assertEqual(ADTConver10P._flt_to_P(0.1, 8, 3), '063')

    def test_do(self):
        self.assertEqual(ADTConver10P.do(10.5, 2, 4), '1010.1000')
        self.assertEqual(ADTConver10P.do(-10.5, 2, 4), '-1010.1000')
        self.assertEqual(ADTConver10P.do(255.999, 16, 2), 'FF.FF')
        self.assertEqual(ADTConver10P.do(0, 8, 2), '0')
        with self.assertRaises(ValueError):
            ADTConver10P.do('abc', 2, 4)
        with self.assertRaises(ValueError):
            ADTConver10P.do(10.5, 17, 4)
        with self.assertRaises(ValueError):
            ADTConver10P.do(10.5, 2, 'abc')

if __name__ == '__main__':
    unittest.main()