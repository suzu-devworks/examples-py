from enum import Enum


class Game(Enum):
    rock = 1
    paper = 2
    scissors = 3

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_string(s: str) -> "Game":
        try:
            return Game[s]
        except KeyError as e:
            raise ValueError(f"key [{s}] is not found") from e
