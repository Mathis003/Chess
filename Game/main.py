import sys
sys.path.append("/Users/mathisdelsart/PycharmProjects/Chess-Game Project/Chess-Game/Game/All_Configs")
from Pieces import Pieces
from Board import Board
from Button import SoundButton, BoardColorButton
from Variables import *
from IA import IA_Player
from Game import Game

# Initialize classes
board = Board(screen)
pieces = Pieces(king_white, king_black)
sound_button = SoundButton(screen, button_sound_on, button_sound_off, button_sound_rect)
board_color_button = BoardColorButton(screen, button_changes_boardcolor, button_changes_boardcolor_rect)
IA_Player = IA_Player()

if __name__ == '__main__': # If the program is run directly, not imported
    game = Game(screen, board, pieces, sound_button, board_color_button, IA_Player) # Create a new game
    game.run() # Run the game