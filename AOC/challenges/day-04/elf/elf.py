from typing import List


class Elf:
    """
    A class to represent an Elf & their assigned sections.
    Sections are input strings as a range. e.g. "3-9". -> [3, 4, 5, 6, 7, 8, 9].
    """
    def __init__(self, assignment_range: str):
        start, end = assignment_range.split("-")
        self.sections: List[int] = [x for x in range(int(start), int(end) + 1)]


    def find_overlap(self, other) -> int:
        """
        Compare one elf's sections to anothers to find overlaps of sections.

        `set(list1) & set(list2)` returns a set of items that appear in both lists.
        If this set isn't empty there's an overlap.

        Args:
            other (Elf): Elf to compare sections with.

        Returns:
            int: 1 or 0 to represent a true/false for overlap.
        """
        return int(len(set(self.sections) & set(other.sections)) > 0)


    def find_full_overlap(self, other) -> int:
        """
        Compare one elf's sections to anothers to find full overlaps of sections.

        `set(list1) & set(list2)` returns a set of items that appear in both lists.
        If this set matches either elf's full section list then there's a full overlap.

        Args:
            other (Elf): Elf to compare sections with.

        Returns:
            int: 1 or 0 to represent a true/false for full overlap.
        """
        overlap: List[int] = sorted(list(set(self.sections) & set(other.sections)))
        return int(overlap == self.sections or overlap == other.sections)
