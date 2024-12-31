class Letter:
    """Representation of a letter in the program."""

    # ATTRIBUTES
    char: str
    state: str

    def __init__(self, char: str) -> None:
        self.char = char.upper()
        self.state = "grey"
