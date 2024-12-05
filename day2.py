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

    def validate_delta(self, levels: list) -> bool:
        for i in range(0, len(levels) - 1):
            #logging.debug(f"Comparing: {levels[i]} and {levels[i+1]}")
            if not (1 <= abs(int(levels[i]) - int(levels[i + 1])) <= 3):
                logging.debug(f"Violation: {levels[i]} - {levels[i+1]}")
                return False
        return True
    
    def validate_direction(self, levels: list) -> bool:
        if levels[0] > levels[1]:
            logging.debug(f"Set direction to down, {levels[0]} > {levels[1]}")
            direction = 'down'
        elif levels[0] < levels[1]:
            logging.debug(f"Set direction to up, {levels[0]} < {levels[1]}")
            direction = 'up'
        else:
            return True
        for i in range(0, len(levels) - 1):
            #print(f"Levels: {levels[i]} vs {levels[i+1]} \t Direction: {direction}")
            if direction == 'down':
                if levels[i] < levels[i+1]:
                    logging.debug(f"Violation: {levels[i]} -> {levels[i+1]} violates direction {direction}")
                    return False
            if direction == 'up':
                if levels[i] > levels[i+1]:
                    logging.debug(f"Violation: {levels[i]} -> {levels[i+1]} violates direction {direction}")
                    return False
        return True

    def part1(self, levels: list) -> int:
        valid_levels = 0
        for level in levels:
            #logging.debug(f"Checking level: {level}")
            valid_delta = self.validate_delta(level)
            valid_direction = self.validate_direction(level)
            if valid_delta and valid_direction:
                valid_levels += 1
            else:
                logging.debug(f"Checking level: {level} \n\t Valid delta: {valid_delta} \n\t Valid direction: {valid_direction}")
                
        return valid_levels
        
if __name__ == "__main__":
    day2 = Day2()