

class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.visited = {(0, 0)}

    @property
    def unique_positions_visited(self):
        return len(self.visited)

    def move_towards(self, x, y):
        # don't move
        if abs(self.x - x) < 2 and abs(self.y - y) < 2:
            return

        # right
        if x > self.x:
            self.x += 1
        # left
        elif x < self.x:
            self.x -= 1
        # up
        if y > self.y:
            self.y += 1
        # down
        elif y < self.y:
            self.y -= 1

        self.visited.add((self.x, self.y))
