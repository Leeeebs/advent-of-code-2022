from typing import List, Generator
from enum import Enum

from .rope import Knot
from logger import create_logger

log = create_logger(__name__)


class Direction(Enum):
    L = (-1, 0)
    R = (1, 0)
    U = (0, 1)
    D = (0, -1)


def main():
    with open("AOC/challenges/day-09/static/puzzle_input.txt") as f:
        movements: Generator[List[str], None, None] = (x.strip().split(" ") for x in f.readlines())

    tail = Knot()
    head_x = 0
    head_y = 0
    for dir, n in movements:
        x, y = Direction[dir].value
        for _ in range(int(n)):
            head_x += x
            head_y += y
            tail.move_towards(head_x, head_y)

    log.info(f"The tail of the rope visits {tail.unique_positions_visited} unique positions!")

    knots = [Knot() for _ in range(9)]
    head_x = 0
    head_y = 0
    for dir, n in movements:
        x, y = Direction[dir].value
        for _ in range(int(n)):
            head_x += x
            head_y += y
            knots[0].move_towards(head_x, head_y)
            knots[1].move_towards(knots[0].x, knots[0].y)
            knots[2].move_towards(knots[1].x, knots[1].y)
            knots[3].move_towards(knots[2].x, knots[2].y)
            knots[4].move_towards(knots[3].x, knots[3].y)
            knots[5].move_towards(knots[4].x, knots[4].y)
            knots[6].move_towards(knots[5].x, knots[5].y)
            knots[7].move_towards(knots[6].x, knots[6].y)
            knots[8].move_towards(knots[7].x, knots[7].y)

    log.info(f"The tail of a 10-knot rope visits {tail.unique_positions_visited} unique positions!")

