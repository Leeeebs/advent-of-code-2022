from typing import List, Union

import names


class Elf:
    """
    A class to represent an elf and it's available calories.
    """
    def __init__(self, id: int, food_items: List[Union[str, int]]):
        """
        Constructor:
            Create a new Elf from an id & a list of calorie values.
            Each elf is assigned a name at random.

        Args:
            id (int): The elf id.
            food_items (List[Union[str, int]]): A list of food item calories
        """
        self.id: int = id
        self.name: str = names.get_first_name()
        self.food_items: List[int] = [int(x.strip("\n")) for x in food_items]

    @property
    def calories(self) -> int:
        """
        Get the total available calories from the elf's food_item list.

        Returns:
            int: the sum of all calories carried by the elf.
        """
        return sum(self.food_items)

    def __str__(self):
        return f"<ELF {self.id}: {self.name}, CALORIES: {self.calories}>"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        return self.calories == other.calories

    def __gt__(self, other):
        return self.calories > other.calories

    def __lt__(self, other):
        return self.calories < other.calories

