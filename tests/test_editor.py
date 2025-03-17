import unittest
from editor import Editor

class TestEditor(unittest.TestCase):
    def setUp(self):
        self.editor = Editor()

    def test_add_digit(self):
        self.editor.add_digit(5)
        self.assertEqual(self.editor.number, "5")
        self.editor.add_digit(10)
        self.assertEqual(self.editor.number, "5A")

    def test_add_zero(self):
        self.editor.add_zero()
        self.assertEqual(self.editor.number, "0")
        self.editor.add_digit(1)
        self.editor.add_zero()
        self.assertEqual(self.editor.number, "010")

    def test_add_delim(self):
        self.editor.add_delim()
        self.assertEqual(self.editor.number, ".")
        self.editor.add_digit(1)
        self.editor.add_delim()
        self.assertEqual(self.editor.number, ".1")

    def test_bs(self):
        self.editor.add_digit(5)
        self.editor.bs()
        self.assertEqual(self.editor.number, "")
        self.editor.add_digit(1)
        self.editor.add_digit(2)
        self.editor.bs()
        self.assertEqual(self.editor.number, "1")

    def test_clear(self):
        self.editor.add_digit(5)
        self.editor.clear()
        self.assertEqual(self.editor.number, "")
        self.editor.add_digit(1)
        self.editor.add_digit(2)
        self.editor.clear()
        self.assertEqual(self.editor.number, "")

    def test_do_edit(self):
        self.assertEqual(self.editor.do_edit(5), "5")
        self.assertEqual(self.editor.do_edit(16), "5.")
        self.assertEqual(self.editor.do_edit(17), "5")
        self.assertEqual(self.editor.do_edit(18), "")

if __name__ == "__main__":
    unittest.main()