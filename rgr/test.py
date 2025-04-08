import unittest
from fractions import Fraction
from memory import CalculatorMemory
from history import CalculatorHistory
from fraction_operations import FractionOperations

class TestFractionOperationsExtended(unittest.TestCase):
    def setUp(self):
        self.ops = FractionOperations()

    def test_parse_edge_cases(self):
        self.assertEqual(self.ops.parse_fraction("1 1/2"), Fraction(3, 2))
        self.assertEqual(self.ops.parse_fraction("-1/2"), Fraction(-1, 2))
        self.assertEqual(self.ops.parse_fraction("1/-2"), Fraction(-1, 2))
        with self.assertRaises(ValueError):
            self.ops.parse_fraction("1e-1")
        with self.assertRaises(ValueError):
            self.ops.parse_fraction("1.2.3")

    def test_format_special_cases(self):
        self.assertEqual(self.ops.format_fraction(Fraction(5, 1)), "5")
        self.assertEqual(self.ops.format_fraction(Fraction(5, 1), "5"))
        self.assertEqual(self.ops.format_fraction(Fraction(-3, 4)), "-3/4")
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_operations_with_large_numbers(self):
        large_num = 123456789
        a = Fraction(large_num, 1)
        b = Fraction(1, large_num)
        self.assertEqual(self.ops.add(a, b), Fraction(large_num**2 + 1, large_num))
        self.assertEqual(self.ops.multiply(a, b), Fraction(1, 1))
        dec_fraction = "0.00000000001"
        f = self.ops.parse_fraction(dec_fraction)
        self.assertEqual(f, Fraction(1, 100000000000))

    def test_mixed_formatting(self):
        value = Fraction(7, 2)
        self.assertEqual(self.ops.format_fraction(value), "7/2")
        self.assertEqual(self.ops.format_fraction(value, "integer"), "3")
        value = Fraction(4, 1)
        self.assertEqual(self.ops.format_fraction(value, "number"), "4")

class IntegrationTests(unittest.TestCase):
    def test_operations_with_parsed_values(self):
        ops = FractionOperations()
        a = ops.parse_fraction("1.5")
        b = ops.parse_fraction("2/3")
        result = ops.multiply(a, b)
        formatted = ops.format_fraction(result)
        self.assertEqual(formatted, "1")

if __name__ == '__main__':
    unittest.main(verbosity=2)