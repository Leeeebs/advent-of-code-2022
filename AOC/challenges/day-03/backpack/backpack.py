import string

from typing import List


class BackpackGroup:
    def __init__(self, item_groups: List[str]) -> None:
        self.backpacks = [Backpack(items) for items in item_groups]

    @property
    def group_priority_sum(self):
        return sum(set([
            Backpack.pos(x) for x in self.backpacks[0].all_items
            if x in self.backpacks[1].all_items and x in self.backpacks[2].all_items
        ]))


class Backpack:
    pos = lambda x: len(string.ascii_letters.split(x)[0]) + 1

    def __init__(self, items: str):
        compartment_limit: int = int(len(items)/2)
        self.all_items: List[str] = [x for x in items if x != "\n"]
        self.compartment_1: List[str] = items[:compartment_limit]
        self.compartment_2: List[str] = items[compartment_limit:]

    @property
    def priority_sum(self):
        return sum(set([
            Backpack.pos(x) for x in self.compartment_1
            if x in self.compartment_2
        ]))

