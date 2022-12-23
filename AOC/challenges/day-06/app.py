from typing import Generator, List, Tuple

from logger import create_logger


log = create_logger(__name__)


def find_marker(input: str, marker_length: int) -> int:
    """
    Loop over input string in chunks & find the marker end position.
    A marker is a group of characters that are all unique.
    """
    is_marker = lambda x, y: len(set(x)) == y

    char_list = []
    start_index = -1
    while not is_marker(char_list, marker_length):
        start_index += 1
        char_list = input[start_index:start_index+marker_length]

    return start_index + marker_length


def main():
    with open("AOC/challenges/day-06/static/puzzle_input.txt") as f:
        input_data: str = f.read()

    marker_pos = find_marker(input_data, marker_length=4)
    log.info(f"marker is complete after {marker_pos} characters have been processed")

    marker_pos = find_marker(input_data, marker_length=14)
    log.info(f"marker is complete after {marker_pos} characters have been processed")

