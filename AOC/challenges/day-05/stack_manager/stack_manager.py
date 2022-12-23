from typing import List, Tuple


class StackManager:
    def __init__(self, stack_data: List[Tuple]) -> None:
        """
        Constructor:
            - create an attr for each stack
            - assign each list from input data & strip empty values
        """
        self.no_of_stacks = len(stack_data)
        for i in range(self.no_of_stacks):
            setattr(self, f"stack_{i+1}", [x for x in stack_data[i] if x != " "])

    @property
    def top_items(self) -> str:
        """Return a string: The last item in each stack, joined."""
        return "".join([getattr(self, f"stack_{i+1}")[-1] for i in range(self.no_of_stacks)])

    def move(self, from_stack: int, to_stack: int) -> None:
        """Remove the last item from one stack & add to another"""
        item = getattr(self, f"stack_{from_stack}").pop()
        getattr(self, f"stack_{to_stack}").append(item)

    def move_group(self, from_stack: int, to_stack: int, amount: int) -> None:
        """Remove a group of items from one stack & add to another"""
        stack = getattr(self, f"stack_{from_stack}")
        getattr(self, f"stack_{to_stack}").extend(stack[-amount:])
        setattr(self, f"stack_{from_stack}", stack[:-amount])
