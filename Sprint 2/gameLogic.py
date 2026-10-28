from copy import deepcopy

#board configurations
english = [[None, None, 1,1,1,None, None],
           [None, None, 1,1,1,None, None],
           [1, 1, 1,    1,    1,   1,  1],
           [1,   1,  1,   0,   1,   1, 1],
           [1,   1,   1,   1,  1,   1, 1],
           [None, None, 1,1,1,None, None],
           [None, None, 1,1,1,None, None]
]
french = [[None, None, 1,1,1,None, None],
          [None, 1,   1,  1,   1,1,None],
          [1, 1, 1,    1,    1,   1,  1],
          [1,   1,  1,   0,   1,   1, 1],
          [1,   1,   1,   1,  1,   1, 1],
          [None, 1,   1,  1,   1,1,None],
          [None, None, 1,1,1,None, None]
]
triangular = [[1],
            [1,1],
            [1,0,1],
            [1,1,1,1],
            [1,1,1,1,1]

]

class PegSolitaire:
    def __init__(self, boardNum=1):
        self.boardNum = boardNum
        if self.boardNum == 1:
            self.board = deepcopy(english)
            self.pegs = 32  # Total number of pegs in the English board
        elif self.boardNum == 2:
            self.board = deepcopy(french)
            self.pegs = 36  # Total number of pegs in the French board
        elif self.boardNum == 3:
            self.board = deepcopy(triangular)
            self.pegs = 14  # Total number of pegs in the Triangular board
        else:
            #current unfinished error handling for invalid board number
            #needs to be tied into UI for user to select a valid board SELECTION, number is on logic side
            raise ValueError("Invalid board number. Please choose a valid board.")

    def is_valid_move(self, fromRow, fromCol, toRow, toCol):
        # Check if the move is within bounds
        if not (0 <= fromRow < len(self.board) and 0 <= fromCol < len(self.board[0]) and
                0 <= toRow < len(self.board) and 0 <= toCol < len(self.board[0])):
            return False

        # Check if the starting position has a peg and the destination is empty
        if self.board[fromRow][fromCol] != 1 or self.board[toRow][toCol] != 0:
            return False

        # Check if the move is a valid jump (two spaces away in a straight line)
        if abs(fromRow - toRow) == 2 and fromCol == toCol:
            midRow = (fromRow + toRow) // 2
            midCol = fromCol
        elif abs(fromCol - toCol) == 2 and fromRow == toRow:
            midRow = fromRow
            midCol = (fromCol + toCol) // 2
        else:
            return False

        # Check if there is a peg in the middle position
        if self.board[midRow][midCol] != 1:
            return False

        return True

    #invalid move handling is not finished in move() func
            # currently outputs "invalid move"
    def move(self, fromRow, fromCol, toRow, toCol):
        # Check if the move is valid
        if not self.is_valid_move(fromRow, fromCol, toRow, toCol):
            raise ValueError("Invalid move.")

        # Perform the move
        self.board[toRow][toCol] = 1
        self.board[fromRow][fromCol] = 0
        self.board[(fromRow + toRow) // 2][(fromCol + toCol) // 2] = 0
        self.pegs -=1

    def is_game_over(self):
        #checking if one peg is left and giving a win if so
        #peg number is tracked in class, decremented in move function
        if self.pegs==1:
            return True #won game
        # Check if there are any valid moves left
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 1:  # If there's a peg at this position
                    # Check all possible jump directions
                    for dRow, dCol in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                        toRow = row + dRow
                        toCol = col + dCol
                        if self.is_valid_move(row, col, toRow, toCol):
                            return False  # Found a valid move

        return True  # No valid moves left
    
    def start_over(self): 
        #reset to original board configuration based on boardNum
        if self.boardNum == 1:
            self.board = deepcopy(english)
            self.pegs = 32  # Total number of pegs in the English board
        elif self.boardNum == 2:
            self.board = deepcopy(french)
            self.pegs = 36  # Total number of pegs in the French board
        elif self.boardNum == 3:
            self.board = deepcopy(triangular)
            self.pegs = 14  # Total number of pegs in the Triangular board