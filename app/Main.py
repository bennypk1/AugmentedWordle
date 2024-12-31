import tkinter as tk

from view.BasicGameView import BasicGameView

if __name__ == '__main__':

    # Initialize root and title
    root = tk.Tk()
    root.title("Augmented Wordle")

    # Initialize the first view frame
    game_view = BasicGameView()
    game_view.pack(fill=tk.BOTH, expand=True)

    # Run the app
    root.mainloop()
