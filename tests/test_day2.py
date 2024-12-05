import unittest
from day2 import Day2

class TestDay2(unittest.TestCase):
    def setUp(self):
        self.day2 = Day2()

    def test_validate_levels(self):
        self.assertTrue(self.day2.validate_levels([1, 2, 3]))
        self.assertTrue(self.day2.validate_levels([3, 2, 1]))
        self.assertTrue(self.day2.validate_levels([1, 4, 7]))
        self.assertFalse(self.day2.validate_levels([3, 1, 4]))
        self.assertFalse(self.day2.validate_levels([2, 3, 4, 3, 2]))

if __name__ == "__main__":
    unittest.main()
