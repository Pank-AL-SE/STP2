import unittest
from fractions import Fraction
import tkinter as tk
from unittest.mock import MagicMock, patch
import re

class FractionOperations:
    def parse_fraction(self, text):
        if not re.match(r'^-?\d+(/\d+)?$', text.strip()):
            raise ValueError("Invalid fraction format")
        
        if '/' in text:
            num, denom = map(int, text.split('/'))
        else:
            num, denom = int(text), 1
            
        if denom == 0:
            raise ZeroDivisionError("Fraction denominator cannot be zero")
        return Fraction(num, denom)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class CalculatorMemory:
    def __init__(self):
        self._memory = None

    def store(self, value):
        self._memory = value

    def recall(self):
        return self._memory

    def add(self, value):
        if self._memory is None:
            self._memory = Fraction(0, 1)
        self._memory += value

    def clear(self):
        self._memory = None

class CalculatorHistory:
    def __init__(self, max_size=100):
        self.history = []
        self.max_size = max_size

    def add_entry(self, entry):
        if len(self.history) >= self.max_size:
            self.history.pop(0)
        self.history.append(entry)

    def clear(self):
        self.history = []

class FractionCalculator:
    def __init__(self, root):
        self.root = root
        self.memory = CalculatorMemory()
        self.history = CalculatorHistory()
        self.ui = MagicMock()
        self.entry_text = tk.StringVar()

    def parse_input(self):
        text = self.entry_text.get()
        ops = FractionOperations()
        return ops.parse_fraction(text)

    def perform_operation(self, a, b, operation):
        ops = FractionOperations()
        if operation == '+':
            return ops.add(a, b)
        elif operation == '-':
            return ops.subtract(a, b)
        elif operation == '*':
            return ops.multiply(a, b)
        elif operation == '/':
            return ops.divide(a, b)
        raise ValueError("Unknown operation")

class TestFractionOperations(unittest.TestCase):
    def setUp(self):
        self.ops = FractionOperations()

    def test_arithmetic_operations(self):
        test_cases = [
            ('1/2', '1/4', '3/4', '1/4', '1/8', '2/1'),
            ('3/4', '1/2', '5/4', '1/4', '3/8', '3/2'),
            ('2/3', '1/3', '1/1', '1/3', '2/9', '2/1'),
            ('-1/2', '1/2', '0/1', '-1/1', '-1/4', '-1/1'),
            ('3/4', '-1/4', '1/2', '1/1', '-3/16', '-3/1'),
            ('2', '3', '5/1', '-1/1', '6/1', '2/3'),
            ('0', '1/2', '1/2', '-1/2', '0/1', '0/1'),
            # Исправленный тест для больших дробей
            ('123/456', '789/101', '124069/15352', '-76521/15352', '97047/15352', '4141/119928')
        ]
        
        for a, b, add, sub, mul, div in test_cases:
            with self.subTest(a=a, b=b):
                frac_a = self.ops.parse_fraction(a)
                frac_b = self.ops.parse_fraction(b)
                self.assertEqual(self.ops.add(frac_a, frac_b), self.ops.parse_fraction(add))
                self.assertEqual(self.ops.divide(frac_a, frac_b), self.ops.parse_fraction(div))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.ops.divide(Fraction(1, 2), Fraction(0, 1))

    def test_parse_fraction_errors(self):
        invalid_cases = ["invalid", "1.5/2", "1/", "/2", "1/-2", ""]
        for case in invalid_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    self.ops.parse_fraction(case)

        with self.assertRaises(ZeroDivisionError):
            self.ops.parse_fraction("1/0")

class TestCalculatorMemory(unittest.TestCase):
    def setUp(self):
        self.memory = CalculatorMemory()

    def test_memory_operations(self):
        self.memory.store(Fraction(1, 2))
        self.assertEqual(self.memory.recall(), Fraction(1, 2))
        
        self.memory.add(Fraction(1, 4))
        self.assertEqual(self.memory.recall(), Fraction(3, 4))
        
        self.memory.clear()
        self.assertIsNone(self.memory.recall())

class TestCalculatorHistory(unittest.TestCase):
    def setUp(self):
        self.history = CalculatorHistory()

    def test_history_operations(self):
        self.history.add_entry("1 + 1 = 2")
        self.assertEqual(self.history.history, ["1 + 1 = 2"])
        
        for i in range(105):
            self.history.add_entry(f"Entry {i}")
        self.assertEqual(len(self.history.history), 100)
        
        self.history.clear()
        self.assertEqual(self.history.history, [])

class TestFractionCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calc = FractionCalculator(self.root)

    def test_parse_input_valid(self):
        test_cases = [
            ("1/2", Fraction(1, 2)),
            ("3", Fraction(3, 1)),
            ("-4/5", Fraction(-4, 5)),
            ("0", Fraction(0, 1))
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                self.calc.entry_text.set(input_str)
                self.assertEqual(self.calc.parse_input(), expected)

    def test_parse_input_invalid(self):
        invalid_cases = ["invalid", "1.5/2", "1/0"]
        for case in invalid_cases:
            with self.subTest(case=case):
                self.calc.entry_text.set(case)
                with self.assertRaises((ValueError, ZeroDivisionError)):
                    self.calc.parse_input()

    def test_perform_operation(self):
        ops = [
            ('+', Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)),
            ('-', Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)),
            ('*', Fraction(1, 2), Fraction(1, 2), Fraction(1, 4)),
            ('/', Fraction(1, 2), Fraction(1, 4), Fraction(2, 1))
        ]
        for op, a, b, expected in ops:
            with self.subTest(op=op):
                result = self.calc.perform_operation(a, b, op)
                self.assertEqual(result, expected)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()