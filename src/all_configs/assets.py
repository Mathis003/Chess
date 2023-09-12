import pygame
from src.all_configs.configs import *


class Asset:
    
    def __init__(self,link_image, dimension):
        self.link_image = link_image
        self.dimension = dimension

    def load_image(self):
        """
        Load the image and transform it with the right dimension
        :return: the image load and transformed
        """
        image = pygame.image.load(self.link_image).convert_alpha()
        image = pygame.transform.scale(image, self.dimension)
        return image


### Load all the assets ###
### 2 differents images for each piece ###

# Black pieces
black_king_image = [Asset("images/pieces/bK.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/king_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
black_queen_image = [Asset("images/pieces/bQ.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/queen_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
black_rook_image = [Asset("images/pieces/bR.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/rook_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
black_bishop_image = [Asset("images/pieces/bB.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/bishop_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
black_knight_image = [Asset("images/pieces/bKN.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/knight_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
black_pawn_image = [Asset("images/pieces/bP.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/pawn_black_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]

# White pieces
white_king_image = [Asset("images/pieces/wK.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/king_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
white_queen_image = [Asset("images/pieces/wQ.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/queen_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
white_rook_image = [Asset("images/pieces/wR.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/rook_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
white_bishop_image = [Asset("images/pieces/wB.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/bishop_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
white_knight_image = [Asset("images/pieces/wKN.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/knight_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]
white_pawn_image = [Asset("images/pieces/wP.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image(), Asset("images/pieces/pawn_white_2.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()]



### Music Sounds ###

pygame.mixer.init()
move_sound = pygame.mixer.Sound("images/music/Move sound.mp3")
capture_sound = pygame.mixer.Sound("images/music/Capture sound.mp3")
castling_sound = pygame.mixer.Sound("images/music/Castling sound.mp3")
check_sound = pygame.mixer.Sound("images/music/Check sound.mp3")
game_start_sound = pygame.mixer.Sound("images/music/Game-Start sound.mp3")
checkmate_sound = pygame.mixer.Sound("images/music/Checkmate sound.mp3")
stalemate_sound = pygame.mixer.Sound("images/music/Stalemate sound.mp3")

# button 'Sound On/Off'
button_sound_on = Asset("images/button/button_sound.png", (SIZE_SQUARE / 2, SIZE_SQUARE / 2)).load_image()
button_sound_off = Asset("images/button/button_sound_off_final.png", (SIZE_SQUARE/ 2, SIZE_SQUARE / 2)).load_image()
button_sound_rect = button_sound_on.get_rect(topleft=(2,2))

# Players images for the begin_menu
player_1 = Asset("images/players/first_player.png", (3 * SIZE_SQUARE, 3 * SIZE_SQUARE)).load_image()
player_2 = Asset("images/players/second_player-removebg-preview.png", (3 * SIZE_SQUARE, 3 * SIZE_SQUARE)).load_image()
player_1_rect_1 = player_1.get_rect(topleft=(3 * SIZE_SQUARE + SIZE_SQUARE / 3, (5/2) * SIZE_SQUARE))
player_2_rect = player_2.get_rect(topleft=(SIZE_SQUARE / 8, (5/2) * SIZE_SQUARE))
player_1_rect_2 = player_1.get_rect(topleft=((9/2) * SIZE_SQUARE + SIZE_SQUARE / 3, (5/2) * SIZE_SQUARE))

# button 'play'
button_play = Asset("images/button/button_play.png", ((2/3) * SIZE_SQUARE, (2/3) * SIZE_SQUARE)).load_image()
button_play_rect_1 = button_play.get_rect(topleft=(6.8 * SIZE_SQUARE + SIZE_SQUARE / 3, (7/2) * SIZE_SQUARE - button_play.get_height() / 2))
button_play_rect_2 = button_play.get_rect(topleft=(2.2 * SIZE_SQUARE + SIZE_SQUARE / 3, (7/2) * SIZE_SQUARE - button_play.get_height() / 2))

# button to change the color of the board
button_changes_boardcolor = Asset("images/button/button_change_mod.png", (SIZE_SQUARE / 2, SIZE_SQUARE / 2)).load_image()
button_changes_boardcolor_rect = button_changes_boardcolor.get_rect(topleft=(COL * SIZE_SQUARE - SIZE_SQUARE / 2 - 2, 2))