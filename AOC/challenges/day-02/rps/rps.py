from enum import IntEnum
from typing import Tuple

class RockPaperSissors:
    """
    A class to represent a round of rock, paper, sissors.
    """
    class Outcome(IntEnum):
        WIN = 6
        DRAW = 3
        LOSS = 0

    class Handsign(IntEnum):
        ROCK = 1
        PAPER = 2
        SISSORS = 3

        @property
        def beats(self):
            """Return the Handsign that loses to this one."""
            match self.value:
                case 1:
                    return RockPaperSissors.Handsign.SISSORS
                case 2:
                    return RockPaperSissors.Handsign.ROCK
                case 3:
                    return RockPaperSissors.Handsign.PAPER

        @property
        def loses_to(self):
            """Return the Handsign that beats this one."""
            match self.value:
                case 1:
                    return RockPaperSissors.Handsign.PAPER
                case 2:
                    return RockPaperSissors.Handsign.SISSORS
                case 3:
                    return RockPaperSissors.Handsign.ROCK

        def vs(self, other):
            """
            Return an Outcome of this handsign vs another, determined by value diff.
                -----------
                rock - rock = 0  (DRAW)
                rock - paper = -1  (LOSS)
                rock - sissors = -2  (WIN)
                -----------
                paper - paper = 0  (DRAW)
                paper - rock = 1  WIN
                paper - sissors = -1  (LOSS)
                -----------
                sissors - sissors = 0  (DRAW)
                sissors - rock = 2  (LOSS)
                sissors - paper = 1  (WIN)
                -----------
                DRAWS = [0, 0, 0]
                WINS = [-2, 1, 1]
                LOSSES = [-1, -1, 2]

            Args:
                other (Handsign): The opposing handsign.
            """
            diff = self.value - other.value

            if diff == 0:
                return RockPaperSissors.Outcome.DRAW
            elif diff in (-2, 1):
                return RockPaperSissors.Outcome.WIN
            elif diff in (-1, 2):
                return RockPaperSissors.Outcome.LOSS

    CHALLENGE_MAPPING = {
        "A": Handsign.ROCK,
        "B": Handsign.PAPER,
        "C": Handsign.SISSORS,
    }

    RESPONSE_MAPPING = {
        "X": Handsign.ROCK,
        "Y": Handsign.PAPER,
        "Z": Handsign.SISSORS,
    }

    OUTCOME_MAPPING = {
        "X": Outcome.LOSS,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }

    @staticmethod
    def get_outcome(opponent: str, player: str) -> Tuple[Handsign, Outcome]:
        """
        Use the mappings to convert the string keys into an Handsign objs.
        Compare the two Handsigns to determine the outcome.

        Args:
            opponent (str): The oppenent's Handsign mapping key.
            player (str): The player's Handsign mapping key.

        Returns:
            Tuple[Handsign, Outcome]: player Handsign obj & an Outcome obj.
        """
        opponent_handsign = RockPaperSissors.CHALLENGE_MAPPING[opponent]
        player_handsign = RockPaperSissors.RESPONSE_MAPPING[player]

        return player_handsign, player_handsign.vs(opponent_handsign)

    @staticmethod
    def force_outcome(opponent: str, outcome: str) -> Tuple[Handsign, Outcome]:
        """
        Use the mappings to convert the string keys into a Handsign obj & Outcome obj.
        Use the objs to return the Handsign required to get the Outcome.

        Args:
            opponent (str): The oppenent's Handsign mapping key.
            outcome (str): The required Outcome mapping key.

        Returns:
            Tuple[Handsign, Outcome]: player Handsign obj & an Outcome obj.
        """
        opponent_handsign = RockPaperSissors.CHALLENGE_MAPPING[opponent]
        outcome = RockPaperSissors.OUTCOME_MAPPING[outcome]

        if outcome == RockPaperSissors.Outcome.LOSS:
            return opponent_handsign.beats, outcome

        if outcome == RockPaperSissors.Outcome.DRAW:
            return opponent_handsign, outcome

        if outcome == RockPaperSissors.Outcome.WIN:
            return opponent_handsign.loses_to, outcome

