from typing import Generator

from .elf import Elf
from logger import create_logger

log = create_logger(__name__)


def get_elf_pairs() -> Generator:
    with open("AOC/challenges/day-04/static/puzzle_input.txt") as f:
        for line in f.readlines():
            assignment_1, assignment_2 = line.split(",")
    yield (Elf(assignment_1), Elf(assignment_2))


def main():
    log.info(f"Full Overlaps: {sum([elf_1.find_full_overlap(elf_2) for elf_1, elf_2 in get_elf_pairs()])}")
    log.info(f"Any Overlaps: {sum([elf_1.find_overlap(elf_2) for elf_1, elf_2 in get_elf_pairs()])}")

