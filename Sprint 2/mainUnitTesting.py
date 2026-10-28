import unittest

from UserInterace import UserInterface 
from gameLogic import PegSolitaire

if __name__ == "__main__":
    # Create a PegSolitaire instance with the English board
    game = PegSolitaire(1)

    # Create a UserInterface instance with the game board
    ui = UserInterface(game.board)

    # Display the initial board configuration
    ui.display_board()
    # for now should just output that its been called

    #game logic unit testing (FIRST MOVE)
    #testing valid moves (based on original english starting board configuration)
    assert game.is_valid_move(5,3,3,3) == True  # Valid first move
    assert game.is_valid_move(3,1,3,3) == True  # Valid first move
    assert game.is_valid_move(3,5,3,3) == True  # Valid first move
    #testing some invalid moves (based on original english starting board configuration)
    assert game.is_valid_move(0, 0, 0, 2) == False  # Invalid move (out of bounds)
    assert game.is_valid_move(2, 0, 2, 1) == False  # Invalid move (not a proper jump) / out of bounds
    assert game.is_valid_move(3, 0, 4, 0) == False  # Invalid move (not a proper jump)
    print("First move tests passed successfully. First move was valid and invalid moves were correctly identified.")


    #unit testting (MOVES following the first move) (saving moves to board)
    game.move(5,3,3,3)  # Perform the first valid move
    assert game.is_valid_move(3,1,3,3) == False  # Invalid move (already moved to center spot
    assert game.is_valid_move(4,1,4,3) == True  #checking next move (valid move)
    game.move(4,1,4,3)  # Perform that valid move
    #check updated board state is accurate after manually calculating
    expected_board_after_moves = [[None, None, 1,1,1,None, None],
                                [None, None, 1,1,1,None, None],
                                [1, 1, 1,    1,    1,   1,  1],
                                [1,   1,  1,   1,   1,   1, 1],
                                [1,   0,   0,   1,  1,   1, 1],
                                [None, None, 1,0,1,None, None],
                                [None, None, 1,1,1,None, None]
]
    assert game.board == expected_board_after_moves, "Board state after moves is incorrect."
    print ("Second round of tests passed successfully. Board state after moves is correct.")


    #stage 3, testing if a board that is out of moves is identified (game over)
    french_board_with_moves_left = [[None, None, 1,0,0,None, None],
                                    [None, 0,   0,  0,   1,0,None],
                                    [0, 0, 0,    0,    0,   0,  0],
                                    [1,   1,  0,   0,   0,   0, 0],
                                    [1,   0,   1,   0,  0,   0, 0],
                                    [None, 1,   1,  0,   1,1,None],
                                    [None, None, 1,0,1,None, None]
                            ]
    game2= PegSolitaire(2)  # Create a new game with the French board
    game2.pegs = 12  # Set the number of pegs to match the test configuration
    game2.board = french_board_with_moves_left  # Set the board to the test configuration
    assert game2.is_game_over() == False, "Game should not be over yet."
    french_board_without_moves_left = [[None, None, 1,0,0,None, None],
                                    [None, 0,   0,  0,   1,0,None],
                                    [0, 0, 1,    0,    0,   0,  0],
                                    [0,   1,  0,   0,   0,   0, 0],
                                    [1,   0,   1,   0,  1,   0, 0],
                                    [None, 1,   0,  0,   0,1,None],
                                    [None, None, 1,0,1,None, None]
                            ]
    game2.pegs = 11
    game2.board = french_board_without_moves_left  # Set the board to the test configuration
    assert game2.is_game_over() == True, "Game should be over."
    winning_french_board         = [[None, None, 0,0,0,None, None],
                                    [None, 0,   0,  0,   0,0,None],
                                    [0, 0, 1,    0,    0,   0,  0],
                                    [0,   0,  0,   0,   0,   0, 0],
                                    [0,   0,   0,   0,  0,   0, 0],
                                    [None, 0,   0,  0,   0,0,None],
                                    [None, None, 0,0,0,None, None]
                            ]
    game2.board = winning_french_board  # Set the board to the test configuration
    game2.pegs = 1
    assert game2.is_game_over() == True, "Game should be over with a win."
    print("Third round, GAME OVER logic tests sucessfully passed")
