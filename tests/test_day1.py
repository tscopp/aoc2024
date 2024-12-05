import unittest
from day1 import Day1

class TestDay1(unittest.TestCase):
    def setUp(self):
        self.day1 = Day1()

    def test_determine_similarity_score(self):
        dataset1 = [1, 2, 3]
        dataset2 = [3, 2, 1]
        result = self.day1.determine_similarity_score(dataset1, dataset2)
        expected_result = [1, 1, 1]
        self.assertEqual(result, expected_result)

    def test_parse_input(self):
        data = ["1   3", "2   2", "3   1"]
        result = self.day1.parse_input(data)
        expected_result = ([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, expected_result)

    def test_part1(self):
        dataset1 = [1, 2, 3]
        dataset2 = [3, 2, 1]
        result = self.day1.part1(dataset1, dataset2)
        expected_result = 4
        self.assertEqual(result, expected_result)

    def test_part2(self):
        similarity_scores = [1, 1, 1]
        dataset1 = [1, 2, 3]
        result = self.day1.part2(similarity_scores, dataset1)
        expected_result = 6
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()