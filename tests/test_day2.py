import unittest
from day2 import Day2

class TestDay2(unittest.TestCase):
    def setUp(self):
        self.day2 = Day2()

    def test_validate_direction(self):
        self.assertTrue(self.day2.validate_direction([1, 2, 3, 4]))
        self.assertTrue(self.day2.validate_direction([4, 3, 2, 1]))
        self.assertFalse(self.day2.validate_direction([1, 3, 2, 4]))
        self.assertFalse(self.day2.validate_direction([4, 1, 3, 2]))

    def test_validate_delta(self):
        self.assertTrue(self.day2.validate_delta([1, 2, 3]))
        self.assertTrue(self.day2.validate_delta([3, 2, 1]))
        self.assertFalse(self.day2.validate_delta([1, 5, 3]))
        self.assertFalse(self.day2.validate_delta([1, 1, 3]))
        self.assertFalse(self.day2.validate_delta([1, 1, 9]))
        self.assertFalse(self.day2.validate_delta([3, 1, 5]))

if __name__ == "__main__":
    unittest.main()
