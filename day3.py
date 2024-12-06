#!/usr/bin/env python3
from util import AOC
import re
import logging

logging.getLogger().setLevel(logging.INFO)

class Day3:
    def __init__(self) -> None:
        aoc = AOC.AOC()
        dataset = aoc.read_input('input/day3.txt')
        print(f"Sum of results: {self.part1(dataset)}")
        print(f"Sum of results for part 2: {self.part2(dataset)}")


    def part2(self, dataset: list) -> int:
        logging.debug(f"Dataset: {dataset}")
        results = []
        enabled = True
        for line in dataset:
            instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
            for i in instructions:
                if i == "do()":
                    enabled = True
                if i == "don't()":
                    enabled = False
                if enabled:
                    if "mul" in i:
                        num1, num2 = map(int, re.findall(r"\d{1,3}", i))
                        results.append(num1 * num2)
        logging.debug(f"Results: {results}")
        return int(sum(results))

    def part1(self, dataset: list) -> int:
        logging.debug(f"Dataset: {dataset}")
        results = []
        pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')

        for line in dataset:
            matches = pattern.findall(line)
            for match in matches:
                num1, num2 = map(int, match)
                results.append(num1 * num2)

        logging.debug(f"Results: {results}")
        return int(sum(results))

if __name__ == "__main__":
    day3 = Day3()