from .backpack import Backpack, BackpackGroup
from logger import create_logger

log = create_logger(__name__)


def split(list_a, group_size):
  for i in range(0, len(list_a), group_size):
    yield list_a[i:i + group_size]


def main():
    with open("AOC/challenges/day-03/static/puzzle_input.txt") as f:
        lines = f.readlines()

    log.info(f"Priority Total: {sum([Backpack(x).priority_sum for x in lines])}")

    log.info(f"Groups Priority Total: {sum([BackpackGroup(x).group_priority_sum for x in split(lines, 3)])}")

