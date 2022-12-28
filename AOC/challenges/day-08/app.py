from typing import List

from .tree_grid import TreeGrid
from logger import create_logger

log = create_logger(__name__)


def main():
    with open("AOC/challenges/day-08/static/puzzle_input.txt") as f:
        input_data: List[str] = [x.strip() for x in f.readlines()]

    trees = TreeGrid(input_data)

    # output: full tree grid to .txt file (for reference, not used anywhere)
    with open("AOC/challenges/day-08/outputs/tree_grid.txt", "w") as f:
        f.writelines(f"{line}\n" for line in trees.height_grid)

    # output: visibility tree grid to .txt file (for reference, not used anywhere)
    with open("AOC/challenges/day-08/outputs/visibility_grid.txt", "w") as f:
        f.writelines(f"{line}\n" for line in trees.visiblility_grid)

    log.info(f"Number of trees visible from the outside = {trees.visible_trees}")

    highest_score = 0
    for row in trees.score_data:
        for val in row:
            if val > highest_score:
                highest_score = val
    log.info(f"The highest scenic score possible for any tree = {highest_score}")
