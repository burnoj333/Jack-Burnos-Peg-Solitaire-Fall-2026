from logging import root
import math
import tkinter as tk
from tkinter import messagebox
from gameLogic import PegSolitaire

#class for peg solitaire user interface
class UserInterface:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Peg Solitaire")
        self.selectedPOS = None  # To store the selected position for moving a peg

        #board selection
        tk.Label(root, text="Select Board Type and Click Start:").pack()
        self.board_type = tk.IntVar(value=1)  # Default to English board
        tk.Radiobutton(root, text="English", variable=self.board_type, value=1).pack()
        tk.Radiobutton(root, text="French", variable=self.board_type, value=2).pack()
        tk.Radiobutton(root, text="Triangular", variable=self.board_type, value=3).pack()

        #start button
        self.start_button = tk.Button(root, text="Start", command=self.start).pack(pady=5)

        #board display area
        self.board_frame = tk.Frame(root)
        self.board_frame.pack(padx=10, pady=10)
        self.status_label = tk.Label(root, text="Starting over resets board").pack(pady=5)

        #start over button
        self.start_over_button = tk.Button(root, text="Start Over", command=self.start_over)
        self.start_over_button.pack(pady=5)

    def start_over(self):
        self.game.start_over()
        self.selectedPOS = None
        self.display_board(self.game.board)

    def display_board(self, board):
        #clear previous board display
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        #display the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell is None:
                    button = tk.Button(self.board_frame, text=" ", width=4, height=2, state=tk.DISABLED, bg="gray")
                elif cell == 1:
                    button = tk.Button(self.board_frame, text=" ", width=4, height=2, command=lambda r=i, c=j: self.positionClicked(r, c), bg="purple", fg="black")
                else:
                    button = tk.Button(self.board_frame, text=" ", width=4, height=2, command=lambda r=i, c=j: self.positionClicked(r, c), bg="white")
                button.grid(row=i, column=j)

        tk.Label(self.board_frame, font = ("Arial", 22), width=2).grid(row=len(board), column=0, columnspan=len(board[0]), pady=10)

    def positionClicked(self, row, col):
        pos = (row, col)
        if self.selectedPOS is None:
            if self.game.board[row][col] == 1:  # Check if there's a peg at the clicked position
                self.selectedPOS = pos
            else:
                return  # Ignore clicks on empty positions
        else:
            start = self.selectedPOS
            end = pos

            #moving / updating display
            self.game.move(start[0], start[1], end[0], end[1])
            self.selectedPOS=None

        self.display_board(self.game.board)

    def start(self):
            board_num = self.board_type.get()
            self.game = PegSolitaire(board_num)
            self.display_board(self.game.board)

    def start_over(self):
        #reset to original board configuration based on boardNum
        self.game.start_over()
        self.selectedPOS = None
        self.display_board(self.game.board)

        