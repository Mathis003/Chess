import pygame

pygame.init()

def CreateWindow():
    from src.configs import WIDTH, HEIGHT

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    from src.assets import black_king_image
    pygame.display.set_icon(black_king_image[0])

    return screen


screen = CreateWindow()

from src.assets import button_sound_on, button_sound_off, button_sound_rect, button_changes_boardcolor, button_changes_boardcolor_rect
from src.pieces import Pieces
from src.board import Board # Represent the board (Draw all tiles correctly with the good color)
from src.button import Sound_Button, BoardColor_Button # Represent the two buttons of the Game to put the sound on/off and to change the board's colors
from src.game import Game # The game himself with the mainloop function


if __name__ == '__main__':

    board = Board(screen)
    sound_button = Sound_Button(screen, button_sound_on, button_sound_off, button_sound_rect, (2 + button_sound_on.get_width() / 2, 2 + button_sound_on.get_width() / 2))
    board_color_button = BoardColor_Button(screen, button_changes_boardcolor, button_changes_boardcolor_rect, (screen.get_width() - 2 - button_changes_boardcolor.get_width() / 2, 2 + button_changes_boardcolor.get_height() / 2))

    game = Game(screen, board, sound_button, board_color_button)
    game.run()