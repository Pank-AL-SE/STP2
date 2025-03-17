import unittest
from history import History

class TestHistory(unittest.TestCase):
    def setUp(self):
        self.history = History()

    def test_add_record(self):
        self.history.add_record(10, 2, "10", "1010")
        self.assertEqual(self.history.count(), 1)
        self.history.add_record(16, 10, "A", "10")
        self.assertEqual(self.history.count(), 2)

    def test_clear(self):
        self.history.add_record(10, 2, "10", "1010")
        self.history.clear()
        self.assertEqual(self.history.count(), 0)
        self.history.add_record(16, 10, "A", "10")
        self.history.clear()
        self.assertEqual(self.history.count(), 0)

if __name__ == "__main__":
    unittest.main()