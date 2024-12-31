import tkinter as tk

class HomePageView(tk.Frame):
    """View for the home page of the application."""
    # TODO: figure out the design

    def __init__(self):
        super().__init__()

        # Initialize TObjects
        self.title_label = tk.Label(self, text="Welcome to Home Page", font=("Arial", 16))
        self.game_button = tk.Button(self, text="Play Wordle", command=self.game_button_click)
        self.suggestion_button = tk.Button(self, text="Wordle Solver", command=self.suggestion_button_click)

        # Pack TObjects
        self.title_label.pack(pady=20)
        self.game_button.pack(pady=10)
        self.suggestion_button.pack(pady=10)

    def game_button_click(self) -> None:
        # TODO: this function
        return

    def suggestion_button_click(self) -> None:
        # TODO: this function
        return
