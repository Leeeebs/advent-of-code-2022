from typing import List


class TreeGrid:
    def __init__(self, input_data: List[str]):
        self.data = [[int(val) for val in line] for  line in input_data]
        self.row_count = len(self.data)
        self.col_count = len(self.data[0])

    def tree(self, row: int, col: int) -> int:
        return self.data[row-1][col-1]

    def trees_to_left(self, row: int, col: int) -> List[int]:
        return self.data[row-1][:col-1]

    def trees_to_right(self, row: int, col: int) -> List[int]:
        return self.data[row-1][col:]

    def trees_above(self, row: int, col: int) -> List[int]:
        return [rows[col-1] for i, rows in enumerate(self.data) if i < row-1]

    def trees_below(self, row: int, col: int) -> List[int]:
        return [rows[col-1] for i, rows in enumerate(self.data) if i > row-1]

    def is_visible(self, row: int, col: int) -> bool:
        """
        Trees on the outside edge are automatically visible.
        Otherwise, For each direction: check if ALL trees are shorter & return True (visible).
        Finally, return True if visibility in ANY direction is True.
        """
        if row in (1, self.row_count) or col in (1, self.col_count):
            return True

        return any([
            all([self.tree(row, col) > other for other in tree_list])
            for tree_list in (
                self.trees_to_left(row, col),
                self.trees_to_right(row, col),
                self.trees_above(row, col),
                self.trees_below(row, col),
            )
        ])

    @property
    def visible_trees(self) -> int:
        return sum([
            self.is_visible(x, y)
            for x in range(1, self.row_count+1)
            for y in range(1, self.col_count+1)
        ])

    def scenic_score(self, row: int, col: int) -> bool:
        """

        """
        score = 1
        for k, tree_list in {
            "left": self.trees_to_left(row, col),
            "right": self.trees_to_right(row, col),
            "up": self.trees_above(row, col),
            "down": self.trees_below(row, col),
        }.items():
            if k in ("left", "up"):
                tree_list.reverse()
            tree_count = 0
            for tree in tree_list:
                tree_count += 1
                if tree >= self.tree(row,col):
                    break
            score = score * tree_count
        return score


    @property
    def height_data(self) -> List[int]:
        """ """
        return [
            [
                self.data[x][y]
                for y in range(self.col_count)
            ]
            for x in range(self.row_count)
        ]

    @property
    def height_grid(self):
        return self.generate_grid_lines(self.height_data)

    @property
    def visiblility_data(self) -> List[str]:
        """ """
        return [
            [
                'o' if self.is_visible(x, y) else 'x'
                for y in range(1, self.col_count+1)
            ]
            for x in range(1, self.row_count+1)
        ]

    @property
    def visiblility_grid(self):
        return self.generate_grid_lines(self.visiblility_data)

    @property
    def score_data(self) -> List[int]:
        """ """
        return [
            [
                self.scenic_score(x, y)
                for y in range(1, self.col_count+1)
            ]
            for x in range(1, self.row_count+1)
        ]

    @property
    def score_grid(self):
        return self.generate_grid_lines(self.score_data)

    def generate_grid_lines(self, grid_data: List[str]):
        return [
            # header
            ".   " + " ".join(str(x).zfill(2) for x in range(1, self.col_count+1)) + "  ",
            ".  +" + "-".join("--" for _ in range(self.col_count)) + "-+",
            *[
                f"{str(i).zfill(2)} | "
                f"{'  '.join([str(val) for val in row])}"
                " |"
                for i, row in enumerate(grid_data, 1)
            ],
            # footer
            ".  +" + "-".join("--" for _ in range(self.col_count)) + "-+",
        ]
