import json
from typing import Dict, Generator, List

from .device import Device
from logger import create_logger

log = create_logger(__name__)


def dir_size_lt(file_tree: Dict, max_size: int) -> Generator:
    """Recursive loop over the file tree to get dir sizes <= max"""
    for directory in file_tree.values():
        size = directory.pop("size")
        if size <= max_size:
            yield size
        for size in dir_size_lt(directory, max_size):
            yield size


def dir_size_gt(file_tree: Dict, min_size: int) -> Generator:
    """Recursive loop over the file tree to get dir sizes >= min"""
    for directory in file_tree.values():
        size = directory.pop("size")
        if size >= min_size:
            yield size
        for size in dir_size_gt(directory, min_size):
            yield size


def main():
    with open("AOC/challenges/day-07/static/puzzle_input.txt") as f:
        input_data: List[str] = f.readlines()

    for line in input_data:
        args: List[str] = [x.strip() for x in line.split(" ") if x]

        if line.startswith("$ cd"):
            Device.cd(args[-1])

        elif line.startswith("dir"):
            Device.add_dir(args[-1])

        elif line[0].isnumeric():
            Device.add_file(*args)

    # output: full file tree to .txt file (for reference, not used anywhere)
    with open("AOC/challenges/day-07/outputs/file_tree.txt", "w") as f:
        json.dump(Device.file_tree(), f, indent=4)

    # output: file tree size breakdown to .txt file (for reference, not used anywhere)
    with open("AOC/challenges/day-07/outputs/file_size.txt", "w") as f:
        json.dump(Device.file_sizes(), f, indent=4)

    # Part 1: result
    log.info(
        "sum of directories with a total size of at most 100000 = "
        f"{sum(dir_size_lt(Device.file_sizes(), max_size=100000))}"
    )

    TOTAL_DISK_SPACE = 70000000
    REQUIRED_SPACE = 30000000
    SPACE_USED = Device.total_size()  # 44376732
    FREE_SPACE = TOTAL_DISK_SPACE - SPACE_USED  # 25623268
    SPACE_TO_DELETE = REQUIRED_SPACE - FREE_SPACE  # 4376732

    # Part 2: result
    log.info(
        "smallest directory that, if deleted, would free up enough space for update = "
        f"{sorted(dir_size_gt(Device.file_sizes(), min_size=SPACE_TO_DELETE))[0]}"
    )
