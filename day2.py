#!/usr/bin/env python3
from util import AOC
import logging

logging.getLogger().setLevel(logging.INFO)

class Day2:
    def __init__(self) -> None:
        aoc = AOC.AOC()
        print(f"Part One: {self.part1(self.parse_input(aoc.read_input('input/day2.txt')))}")
        
    def parse_input(self, input_data: str) -> list:
        global_levels = []
        for line in input_data:
            local_levels = [int(x) for x in line.split()]
            global_levels.append(local_levels)
        return global_levels

    def delta(self, level1: list, level2: list) -> int:
        return abs(int(level1[0]) - int(level2[0]))

    def validate_levels(self, levels: list) -> bool:
        if levels[0] > levels[1]:
            logging.debug(f"Set direction to down, {levels[0]} > {levels[1]}")
            direction = 'down'
        elif levels[0] < levels[1]:
            logging.debug(f"Set direction to up, {levels[0]} < {levels[1]}")
            direction = 'up'        
        for i in range(1, len(levels)):
            #logging.debug(f"Comparing: {levels[i-1]} and {levels[i]}")
            if not (1 <= abs(int(levels[i-1]) - int(levels[i])) <= 3):
                logging.debug(f"Violation: {levels[i-1]} - {levels[i]}")
                return False
            if direction == 'down':
                if levels[i-1] < levels[i]:
                    logging.debug(f"Violation: {levels[i-1]} -> {levels[i]} violates direction {direction}")
                    return False
            if direction == 'up':
                if levels[i-1] > levels[i]:
                    logging.debug(f"Violation: {levels[i-1]} -> {levels[i]} violates direction {direction}")
                    return False
        return True

    def part1(self, levels: list) -> int:
        valid_levels = 0
        for level in levels:
            logging.debug(f"Checking level: {level}")
            if self.validate_levels(level):
                valid_levels += 1
                
        return valid_levels
        
if __name__ == "__main__":
    day2 = Day2()