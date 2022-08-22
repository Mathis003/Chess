import sys
import pygame
sys.path.append("/Users/mathisdelsart/PycharmProjects/Chess-Game Project/Chess-Game/Game/All_Configs")

def CreateWindow():
    from Configs import WIDTH, HEIGHT

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    from Assets import black_king_image  # Assets file need the screen initialized to load all the images !

    # Set the icon of the window (the black piece's image)
    pygame.display.set_icon(black_king_image)

    return screen

# Initialize the window
screen = CreateWindow()

# Import all the necessary file
from Pieces import Pieces # All the functions associated to the movements of the pieces
from Board import Board # Represent the board (Draw all tiles correctly with the good color)
from Button import SoundButton, BoardColorButton # Represent the two buttons of the Game to put the sound on/off
                                                 # and to change the board's colors
from IA import IA_Player # All the functions associated with the IA Player
from Game import Game # The game himself with the mainloop function
from Variables import king_white, king_black, button_sound_on, button_sound_off, button_sound_rect,\
                      button_changes_boardcolor, button_changes_boardcolor_rect # Import the necessary 'tools' to
                                                                                # initialyze correctly the classes

# Initialize classes
board = Board(screen)
pieces = Pieces(king_white, king_black)
sound_button = SoundButton(screen, button_sound_on, button_sound_off, button_sound_rect)
board_color_button = BoardColorButton(screen, button_changes_boardcolor, button_changes_boardcolor_rect)
IA_Player = IA_Player()

### PROGRAM ###
if __name__ == '__main__': # If the program is run directly, not imported
    pygame.init()
    game = Game(screen, board, pieces, sound_button, board_color_button, IA_Player) # Create a new game
    game.run_mainloop() # Run the game