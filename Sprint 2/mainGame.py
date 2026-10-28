from UserInterace import UserInterface
from gameLogic import PegSolitaire

import tkinter as tk

# class MainGame:
#     def __init__(self,root):
#         self.root = root
#         self.game = PegSolitaire()
#         self.ui = UserInterface(root)

#     def start(self, board_num):
#         self.game.boardNum = board_num
#         self.game.start_over()  # Reset the game to the initial configuration


if __name__ == "__main__":
    root = tk.Tk()
    game = PegSolitaire()
    ui = UserInterface(root)
    root.mainloop()