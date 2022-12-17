from typing import List, Generator

from .rps import RockPaperSissors
from logger import create_logger

log = create_logger(__name__)


def get_data() -> Generator:
    """
    Read the input file & process lines.

    Yields:
        Generator: file lines split into lists of 2 str values.
    """
    with open("AOC/challenges/day-02/static/puzzle_input.txt") as f:
        lines = f.readlines()

    for x in lines:
        yield x.strip("\n").split(" ")


def main():
    results: List[int] = [sum(RockPaperSissors.get_outcome(*group)) for group in get_data()]
    log.info(f"RESULTS OF THE TOURNAMENT (PART 1): {sum(results)}")

    results: List[int] = [sum(RockPaperSissors.force_outcome(*group)) for group in get_data()]
    log.info(f"RESULTS OF THE TOURNAMENT (PART 2): {sum(results)}")

