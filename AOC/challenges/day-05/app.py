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
        yield tuple(int(x.strip()) for x in line.split(" ") if x.strip().isnumeric())


def main():
    with open("AOC/challenges/day-05/static/puzzle_input.txt") as f:
        input_data: List[str] = f.readlines()

    sm_1 = StackManager(list(parse_stacks(input_data)))

    for amount, stack1, stack2 in parse_instructions(input_data):
        for _ in range(amount):
            sm_1.move(from_stack=stack1, to_stack=stack2)

    log.info(f"PART 1 - top crates: {sm_1.top_items}")


    sm_2 = StackManager(list(parse_stacks(input_data)))

    for amount, stack1, stack2 in parse_instructions(input_data):
        sm_2.move_group(from_stack=stack1, to_stack=stack2, amount=amount)

    log.info(f"PART 2 - top crates: {sm_2.top_items}")

