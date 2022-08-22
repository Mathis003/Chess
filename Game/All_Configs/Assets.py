import pygame
from Configs import *

"""Asset Class for all images"""
class Asset:
    """ Represent the image in the game """
    def __init__(self,link_image, dimension):
        self.link_image = link_image
        self.dimension = dimension

    def load_image(self):
        image = pygame.image.load(self.link_image).convert_alpha()
        image = pygame.transform.scale(image, self.dimension)
        return image

### Load all the assets ###

# Black pieces 1
black_king_image = Asset("All_Assets/Pieces_image/bK.png", (SQUARE, SQUARE)).load_image()
black_queen_image = Asset("All_Assets/Pieces_image/bQ.png", (SQUARE, SQUARE)).load_image()
black_rook_image = Asset("All_Assets/Pieces_image/bR.png", (SQUARE, SQUARE)).load_image()
black_bishop_image = Asset("All_Assets/Pieces_image/bB.png", (SQUARE, SQUARE)).load_image()
black_knight_image = Asset("All_Assets/Pieces_image/bKN.png", (SQUARE, SQUARE)).load_image()
black_pawn_image = Asset("All_Assets/Pieces_image/bP.png", (SQUARE, SQUARE)).load_image()

# White pieces 1
white_king_image = Asset("All_Assets/Pieces_image/wK.png", (SQUARE, SQUARE)).load_image()
white_queen_image = Asset("All_Assets/Pieces_image/wQ.png", (SQUARE, SQUARE)).load_image()
white_rook_image = Asset("All_Assets/Pieces_image/wR.png", (SQUARE, SQUARE)).load_image()
white_bishop_image = Asset("All_Assets/Pieces_image/wB.png", (SQUARE, SQUARE)).load_image()
white_knight_image = Asset("All_Assets/Pieces_image/wKN.png", (SQUARE, SQUARE)).load_image()
white_pawn_image = Asset("All_Assets/Pieces_image/wP.png", (SQUARE, SQUARE)).load_image()

# Black pieces 2
black_king_image_2 = Asset("All_Assets/Pieces_image/king_black_2.png", (SQUARE, SQUARE)).load_image()
black_queen_image_2 = Asset("All_Assets/Pieces_image/queen_black_2.png", (SQUARE, SQUARE)).load_image()
black_rook_image_2 = Asset("All_Assets/Pieces_image/rook_black_2.png", (SQUARE, SQUARE)).load_image()
black_bishop_image_2 = Asset("All_Assets/Pieces_image/bishop_black_2.png", (SQUARE, SQUARE)).load_image()
black_knight_image_2 = Asset("All_Assets/Pieces_image/knight_black_2.png", (SQUARE, SQUARE)).load_image()
black_pawn_image_2 = Asset("All_Assets/Pieces_image/pawn_black_2.png", (SQUARE, SQUARE)).load_image()

# White pieces 2
white_king_image_2 = Asset("All_Assets/Pieces_image/king_white_2.png", (SQUARE, SQUARE)).load_image()
white_queen_image_2 = Asset("All_Assets/Pieces_image/queen_white_2.png", (SQUARE, SQUARE)).load_image()
white_rook_image_2 = Asset("All_Assets/Pieces_image/rook_white_2.png", (SQUARE, SQUARE)).load_image()
white_bishop_image_2 = Asset("All_Assets/Pieces_image/bishop_white_2.png", (SQUARE, SQUARE)).load_image()
white_knight_image_2 = Asset("All_Assets/Pieces_image/knight_white_2.png", (SQUARE, SQUARE)).load_image()
white_pawn_image_2 = Asset("All_Assets/Pieces_image/pawn_white_2.png", (SQUARE, SQUARE)).load_image()

# Musics
pygame.mixer.init()
move_sound = pygame.mixer.Sound("All_Assets/Music/Move sound.mp3")
capture_sound = pygame.mixer.Sound("All_Assets/Music/Capture sound.mp3")
castling_sound = pygame.mixer.Sound("All_Assets/Music/Castling sound.mp3")
check_sound = pygame.mixer.Sound("All_Assets/Music/Check sound.mp3")
game_start_sound = pygame.mixer.Sound("All_Assets/Music/Game-Start sound.mp3")
checkmate_sound = pygame.mixer.Sound("All_Assets/Music/Checkmate sound.mp3")
stalemate_sound = pygame.mixer.Sound("All_Assets/Music/Stalemate sound.mp3")

# Button Sound On/Off
button_sound_on = Asset("All_Assets/Button/button_sound.png", (SQUARE / 2, SQUARE / 2)).load_image()
button_sound_off = Asset("All_Assets/Button/button_sound_off_final.png", (SQUARE/ 2, SQUARE / 2)).load_image()
button_sound_rect = button_sound_on.get_rect(topleft=(2,2))

# Players
player_1 = Asset("All_Assets/Players/first_player.png", (3 * SQUARE, 3 * SQUARE)).load_image()
player_2 = Asset("All_Assets/Players/second_player-removebg-preview.png", (3 * SQUARE, 3 * SQUARE)).load_image()
player_1_rect_1 = player_1.get_rect(topleft=(3 * SQUARE + SQUARE / 3, (5/2) * SQUARE))
player_2_rect = player_2.get_rect(topleft=(SQUARE / 8, (5/2) * SQUARE))
player_1_rect_2 = player_1.get_rect(topleft=((9/2) * SQUARE + SQUARE / 3, (5/2) * SQUARE))

# Button play
button_play = Asset("All_Assets/Button/button_play.png", ((2/3) * SQUARE, (2/3) * SQUARE)).load_image()
button_play_rect_1 = button_play.get_rect(topleft=(6.8 * SQUARE + SQUARE / 3, (7/2) * SQUARE - button_play.get_height() / 2))
button_play_rect_2 = button_play.get_rect(topleft=(2.2 * SQUARE + SQUARE / 3, (7/2) * SQUARE - button_play.get_height() / 2))

# Button to change the color of the board
button_changes_boardcolor = Asset("All_Assets/Button/button_change_mod.png", (SQUARE / 2, SQUARE / 2)).load_image()
button_changes_boardcolor_rect = button_changes_boardcolor.get_rect(topleft=(COL * SQUARE - SQUARE / 2 - 2, 2))