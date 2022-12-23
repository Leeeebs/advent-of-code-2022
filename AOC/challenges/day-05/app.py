from typing import Generator, List, Tuple

from .stack_manager import StackManager
from logger import create_logger


log = create_logger(__name__)


def parse_stacks(file_data: List[str], end_line: int = 8) -> zip:
    """Parse stack data from the first few rows"""
    # parse stack data from top to bottom
    stack_rows = [
        [line[i] for i in (1, 5, 9, 13, 17, 21, 25, 29, 33)]
        for line in file_data[:end_line]
    ]
    # reverse order to get stack data bottom-to-top
    stack_rows.reverse()
    # zip the rows to generate stack columns as tuples
    return zip(*stack_rows)


def parse_instructions(file_data: List[str], start_line: int = 11) -> Generator:
    """Parse instructions from the rest of the file"""
    for line in file_data[start_line-1:]:
        yield tuple(x.strip() for x in line.split(" ") if x.strip().isnumeric())


def main():
    with open("AOC/challenges/day-05/static/puzzle_input.txt") as f:
        input_data: List[str] = f.readlines()

    sm = StackManager(list(parse_stacks(input_data)))
    for amount, stack1, stack2 in parse_instructions(input_data):
        [
            sm.move(from_stack=int(stack1), to_stack=int(stack2))
            for _ in range(int(amount))
        ]

    log.info(f"top crates: {sm.top_items}")

