from Pieces import Pieces
from Board import Board
from Assets import screen, king_white, king_black
from Game import Game

# Initialize classes
board = Board(screen)
pieces = Pieces(king_white, king_black)

if __name__ == '__main__': # If the program is run directly, not imported
    game = Game(screen, board, pieces) # Create a new game
    game.run() # Run the game