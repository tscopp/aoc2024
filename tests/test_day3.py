
import unittest
from day3 import Day3

class TestDay3(unittest.TestCase):
    def setUp(self):
        self.day3 = Day3()

    def test_part1(self):
        dataset = [
            "mul(2,3)",
            "mul(4,5)",
            "mul(6,7)"
        ]
        result = self.day3.part1(dataset)
        self.assertEqual(result, 2*3 + 4*5 + 6*7)

    def test_part2(self):
        dataset = [
            "do()",
            "mul(2,3)",
            "don't()",
            "mul(4,5)",
            "do()",
            "mul(6,7)"
        ]
        result = self.day3.part2(dataset)
        self.assertEqual(result, 2*3 + 6*7)

if __name__ == "__main__":
    unittest.main()