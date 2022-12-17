from typing import List, Generator

from .elf import Elf
from logger import create_logger

log = create_logger(__name__)


def get_data() -> Generator:
    # read in the textfile lines
    with open("AOC/challenges/day-01/static/puzzle_input.txt") as f:
        lines: List[str] =  f.readlines()

    # find all the lines that are "newline" separators
    separator_indices: List[int] = [i for i, x in enumerate(lines) if x == "\n"]

    # zip groups by indecies, adjust to remove the seperator value.
    for start, end in zip([-1, *separator_indices], [*separator_indices, len(lines)]):
        yield lines[start+1:end]


def main():
    # build list of Elf objects from generator, sorted lowest to highest calories.
    elves: List[Elf] = sorted([Elf(i, data) for i, data in enumerate(get_data(), 1)])
    log.debug(f"There are {len(elves)} happy little elves!")

    # find the elf with the highest calories by printing the last in the list.
    log.info(f"ELF WITH THE HIGHEST CALORIES IS: {elves[-1]}")

    # find the total calories from the 3 elves carrying the most calories.
    log.info(f"TOTAL CALORIES FROM THE 3 HIGHEST: {sum([x.calories for x in elves[-3:]])}")

