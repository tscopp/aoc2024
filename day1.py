#!/usr/bin/env python3
import AOC


class Day1:
    def __init__(self) -> None:
        aoc = AOC.AOC()
        dataset1, dataset2 = self.parse_input(aoc.read_input('day1.txt'))
        print(f"Part One: {self.part1(dataset1, dataset2)}")
        print(f"Part Two: {self.part2(self.determine_similarity_score(dataset1, dataset2), dataset1)}")

    def determine_similarity_score(self, dataset1: list, dataset2: list) -> list:
        similarity_scores = []
        for i in range(0, len(dataset1)):
            similarity_score = 0
            for j in range(0, len(dataset1)):
                if dataset1[i] == dataset2[j]:
                    similarity_score += 1
            similarity_scores.append(similarity_score)
        return similarity_scores 

    def parse_input(self, data: list) -> list:
        dataset1, dataset2 = [], []
        for entry in data:
            entry1, entry2 = entry.split('   ')
            dataset1.append(entry1)
            dataset2.append(entry2)
        dataset1 = list(map(int, dataset1))
        dataset2 = list(map(int, dataset2))
        dataset1.sort()
        dataset2.sort()   
        return dataset1, dataset2     

    def parse_input(self, data: list) -> list:
        dataset1, dataset2 = [], []
        for entry in data:
            entry1, entry2 = entry.split('   ')
            dataset1.append(entry1)
            dataset2.append(entry2)
        dataset1 = list(map(int, dataset1))
        dataset2 = list(map(int, dataset2))
        dataset1.sort()
        dataset2.sort()   
        return dataset1, dataset2     

    def part2(self, similarity_scores: list, dataset1: list) -> int:
        aggregate_similarity_score = 0
        for i in range(0, len(dataset1)):
            aggregate_similarity_score += dataset1[i] * similarity_scores[i]
        return aggregate_similarity_score

    def part1(self, dataset1: list, dataset2: list) -> float:
        deltas = []
        for i in range(0, len(dataset1)):
            if dataset1[i] > dataset2[i]:
                deltas.append(dataset1[i] - dataset2[i])
            elif dataset2[i] > dataset1[i]:
                deltas.append(dataset2[i] - dataset1[i])
        total_delta = 0
        for delta in deltas:
            total_delta += delta   
        return total_delta

if __name__ == "__main__":
    day1 = Day1()