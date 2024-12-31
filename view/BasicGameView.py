import tkinter as tk


class BasicGameView(tk.Frame):
    """View for playing the base game."""
    # TODO: figure out the design

    def __init__(self):
        super().__init__()

        # Initialize and pack the return to home button, and the reset button
        home_button = tk.Button(self, text="Exit", command=self.return_home)
        home_button.grid(column=0, row=0, columnspan=2)

        reset_button = tk.Button(self, text="Reset", command=self.reset)
        reset_button.grid(column=2, row=0, columnspan=3)

        # Initialize and pack the entries
        for row in range(6):
            entry = tk.Entry(self, width=15, font=("Helvetica", 40))
            entry.grid(row=row+1, column=0, columnspan=5)
            entry.bind("<Return>", lambda event, e=entry, r=row: self.on_enter(e, r))

    def on_enter(self, entry, row_index) -> None:
        # TODO: this function, remember to output an error message if invalid input
        pass

    def return_home(self) -> None:
        # TODO: this function
        pass

    def reset(self) -> None:
        # TODO: this function
        pass
