import Letter

class Word:
    """Representation of a Word in the program."""

    # ATTRIBUTES:
    representation: str
    letters: list[Letter]
    correct: bool

    def __init__(self, word: str) -> None:
        self.letters = []
        self.correct = False
        self.representation = word
        for char in word:
            self.letters.append(Letter(char))
