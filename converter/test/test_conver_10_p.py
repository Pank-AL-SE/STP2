import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from libs.conver_10_p import Conver10P

class TestConver10P(unittest.TestCase):

    def test_dval_positive(self):
        self.assertAlmostEqual(Conver10P.dval("A5.E", 16), 165.875)
        self.assertAlmostEqual(Conver10P.dval("FF.A", 16), 255.625)
        self.assertAlmostEqual(Conver10P.dval("11.1", 2), 3.5)

    def test_dval_negative(self):
        self.assertAlmostEqual(Conver10P.dval("-A5.E", 16), -165.875)
        self.assertAlmostEqual(Conver10P.dval("-FF.A", 16), -255.625)
        self.assertAlmostEqual(Conver10P.dval("-11.1", 2), -3.5)

if __name__ == '__main__':
    unittest.main()