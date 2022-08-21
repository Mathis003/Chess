from Pieces import Pieces
from Board import Board
from Button import SoundButton, BoardColorButton
from Assets import screen, king_white, king_black, button_sound_on, button_sound_off, button_sound_rect,\
                   button_changes_boardcolor, button_changes_boardcolor_rect
from Game import Game

# Initialize classes
board = Board(screen)
pieces = Pieces(king_white, king_black)
sound_button = SoundButton(screen, button_sound_on, button_sound_off, button_sound_rect)
board_color_button = BoardColorButton(screen, button_changes_boardcolor, button_changes_boardcolor_rect)

if __name__ == '__main__': # If the program is run directly, not imported
    game = Game(screen, board, pieces, sound_button, board_color_button) # Create a new game
    game.run() # Run the game