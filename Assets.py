import pygame
from Configs import *

"""Asset Class for all images"""
class Asset:
    """ Represent the image in the game """
    def __init__(self,link_image, dimension):
        self.link_image = link_image
        self.dimension = dimension

    def load_image_rect(self):
        image = pygame.image.load(self.link_image)
        image = pygame.transform.scale(image, self.dimension)
        rect_image = image.get_rect()
        return image, rect_image

# Load all the assets

# Black pieces
black_king_image, black_king_rect = Asset("Pieces_image/bK.png", (SQUARE, SQUARE)).load_image_rect()
black_queen_image, black_queen_rect = Asset("Pieces_image/bQ.png", (SQUARE, SQUARE)).load_image_rect()
black_rook_image, black_rook_rect = Asset("Pieces_image/bR.png", (SQUARE, SQUARE)).load_image_rect()
black_bishop_image, black_bishop_rect = Asset("Pieces_image/bB.png", (SQUARE, SQUARE)).load_image_rect()
black_knight_image, black_knight_rect = Asset("Pieces_image/bKN.png", (SQUARE, SQUARE)).load_image_rect()
black_pawn_image, black_pawn_rect = Asset("Pieces_image/bP.png", (SQUARE, SQUARE)).load_image_rect()

# White pieces
white_king_image, white_king_rect = Asset("Pieces_image/wK.png", (SQUARE, SQUARE)).load_image_rect()
white_queen_image, white_queen_rect = Asset("Pieces_image/wQ.png", (SQUARE, SQUARE)).load_image_rect()
white_rook_image, white_rook_rect = Asset("Pieces_image/wR.png", (SQUARE, SQUARE)).load_image_rect()
white_bishop_image, white_bishop_rect = Asset("Pieces_image/wB.png", (SQUARE, SQUARE)).load_image_rect()
white_knight_image, white_knight_rect = Asset("Pieces_image/wKN.png", (SQUARE, SQUARE)).load_image_rect()
white_pawn_image, white_pawn_rect = Asset("Pieces_image/wP.png", (SQUARE, SQUARE)).load_image_rect()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""
Dictionnary :
    key : tile coordinate
    value : list with : object (piece), image_of_the_piece, number_of_the_piece, list_of_possibile_moves
"""

def create_pieces():
    from all_pieces import Rook, Bishop, Knight, Queen, King, Pawn
    """All the Classes"""
    # Rook
    white_rook_rect.topleft = (0, 7 * SQUARE)
    rook_white_1 = Rook(white_rook_rect, [7, 0], -1)
    white_rook_rect.topleft = (7 * SQUARE, 7 * SQUARE)
    rook_white_2 = Rook(white_rook_rect, [7, 7], -1)
    black_rook_rect.topleft = (0, 0)
    rook_black_1 = Rook(black_rook_rect, [0, 0], 1)
    black_rook_rect.topleft = (7 * SQUARE, 0)
    rook_black_2 = Rook(black_rook_rect, [0, 7], 1)
    # Bishop
    white_bishop_rect.topleft = (2 * SQUARE, 7 * SQUARE)
    bishop_white_1 = Bishop(white_bishop_rect, [7, 2], -1)
    white_bishop_rect.topleft = (5 * SQUARE, 7 * SQUARE)
    bishop_white_2 = Bishop(white_bishop_rect, [7, 5], -1)
    black_bishop_rect.topleft = (7 * SQUARE, 2 * SQUARE)
    bishop_black_1 = Bishop(black_bishop_rect, [0, 2], 1)
    black_bishop_rect.topleft = (7 * SQUARE, 5 * SQUARE)
    bishop_black_2 = Bishop(black_bishop_rect, [0, 5], 1)
    # Queen
    white_queen_rect.topleft = (3 * SQUARE, 7 * SQUARE)
    queen_white = Queen(white_queen_rect, [7, 3], -1)
    black_queen_rect.topleft = (7 * SQUARE, 3 * SQUARE)
    queen_black = Queen(black_queen_rect, [0, 3], 1)
    # King
    white_king_rect.topleft = (4 * SQUARE, 7 * SQUARE)
    king_white = King(white_king_rect, [7, 4], -1)
    black_king_rect.topleft = (7 * SQUARE, 4 * SQUARE)
    king_black = King(black_king_rect, [0, 4], 1)
    # Knight
    white_knight_rect.topleft = (1 * SQUARE, 7 * SQUARE)
    knight_white_1 = Knight(white_knight_rect, [7, 1], -1)
    white_knight_rect.topleft = (6 * SQUARE, 7 * SQUARE)
    knight_white_2 = Knight(white_knight_rect, [7, 6], -1)
    black_knight_rect.topleft = (7 * SQUARE, 1 * SQUARE)
    knight_black_1 = Knight(black_knight_rect, [0, 1], 1)
    black_knight_rect.topleft = (7 * SQUARE, 6 * SQUARE)
    knight_black_2 = Knight(black_knight_rect, [0, 6], 1)
    # Pawn
    white_pawn_rect.topleft = (0, 6 * SQUARE)
    pawn_white_1 = Pawn(white_pawn_rect, [6, 0], -1, True)
    white_pawn_rect.topleft = (1 * SQUARE, 6 * SQUARE)
    pawn_white_2 = Pawn(white_pawn_rect, [6, 1], -1, True)
    white_pawn_rect.topleft = (2 * SQUARE, 6 * SQUARE)
    pawn_white_3 = Pawn(white_pawn_rect, [6, 2], -1, True)
    white_pawn_rect.topleft = (3 * SQUARE, 6 * SQUARE)
    pawn_white_4 = Pawn(white_pawn_rect, [6, 3], -1, True)
    white_pawn_rect.topleft = (4 * SQUARE, 6 * SQUARE)
    pawn_white_5 = Pawn(white_pawn_rect, [6, 4], -1, True)
    white_pawn_rect.topleft = (5 * SQUARE, 6 * SQUARE)
    pawn_white_6 = Pawn(white_pawn_rect, [6, 5], -1, True)
    white_pawn_rect.topleft = (6 * SQUARE, 6 * SQUARE)
    pawn_white_7 = Pawn(white_pawn_rect, [6, 6], -1, True)
    white_pawn_rect.topleft = (7 * SQUARE, 6 * SQUARE)
    pawn_white_8 = Pawn(white_pawn_rect, [6, 7], -1, True)
    black_pawn_rect.topleft = (0, 1 * SQUARE)
    pawn_black_1 = Pawn(black_pawn_rect, [1, 0], 1, True)
    black_pawn_rect.topleft = (1 * SQUARE, 1 * SQUARE)
    pawn_black_2 = Pawn(black_pawn_rect, [1, 1], 1, True)
    black_pawn_rect.topleft = (2 * SQUARE, 1 * SQUARE)
    pawn_black_3 = Pawn(black_pawn_rect, [1, 2], 1, True)
    black_pawn_rect.topleft = (3 * SQUARE, 1 * SQUARE)
    pawn_black_4 = Pawn(black_pawn_rect, [1, 3], 1, True)
    black_pawn_rect.topleft = (4 * SQUARE, 1 * SQUARE)
    pawn_black_5 = Pawn(black_pawn_rect, [1, 4], 1, True)
    black_pawn_rect.topleft = (5 * SQUARE, 1 * SQUARE)
    pawn_black_6 = Pawn(black_pawn_rect, [1, 5], 1, True)
    black_pawn_rect.topleft = (6 * SQUARE, 1 * SQUARE)
    pawn_black_7 = Pawn(black_pawn_rect, [1, 6], 1, True)
    black_pawn_rect.topleft = (7 * SQUARE, 1 * SQUARE)
    pawn_black_8 = Pawn(black_pawn_rect, [1, 7], 1, True)

    return rook_white_1, rook_white_2, rook_black_1, rook_black_2,\
           bishop_white_1, bishop_white_2, bishop_black_1, bishop_black_2,\
           queen_white, queen_black, king_white, king_black, knight_white_1,\
           knight_white_2, knight_black_1, knight_black_2, pawn_white_1, pawn_white_2,\
           pawn_white_3, pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8,\
           pawn_black_1, pawn_black_2, pawn_black_3, pawn_black_4, pawn_black_5, pawn_black_6,\
           pawn_black_7, pawn_black_8


def create_dico_board():

    dico_board = {(0, 0): [rook_black_1, black_rook_image, -1, []],
                  (0, 1): [knight_black_1, black_knight_image, -1, []],
                  (0, 2): [bishop_black_1, black_bishop_image, -1, []],
                  (0, 3): [queen_black, black_queen_image, -1, []], (0, 4): [king_black, black_king_image, -2, []],
                  (0, 5): [bishop_black_2, black_bishop_image, -1, []],
                  (0, 6): [knight_black_2, black_knight_image, -1, []],
                  (0, 7): [rook_black_2, black_rook_image, -1, []],
                  (1, 0): [pawn_black_1, black_pawn_image, -1, []], (1, 1): [pawn_black_2, black_pawn_image, -1, []],
                  (1, 2): [pawn_black_3, black_pawn_image, -1, []], (1, 3): [pawn_black_4, black_pawn_image, -1, []],
                  (1, 4): [pawn_black_5, black_pawn_image, -1, []], (1, 5): [pawn_black_6, black_pawn_image, -1, []],
                  (1, 6): [pawn_black_7, black_pawn_image, -1, []], (1, 7): [pawn_black_8, black_pawn_image, -1, []],
                  (2, 0): [None, None, 0, []], (2, 1): [None, None, 0, []], (2, 2): [None, None, 0, []], (2, 3): [None, None, 0, []], (2, 4): [None, None, 0, []],
                  (2, 5): [None, None, 0, []], (2, 6): [None, None, 0, []], (2, 7): [None, None, 0, []],
                  (3, 0): [None, None, 0, []], (3, 1): [None, None, 0, []], (3, 2): [None, None, 0, []], (3, 3): [None, None, 0, []], (3, 4): [None, None, 0, []],
                  (3, 5): [None, None, 0, []], (3, 6): [None, None, 0, []], (3, 7): [None, None, 0, []],
                  (4, 0): [None, None, 0, []], (4, 1): [None, None, 0, []], (4, 2): [None, None, 0, []], (4, 3): [None, None, 0, []], (4, 4): [None, None, 0, []],
                  (4, 5): [None, None, 0, []], (4, 6): [None, None, 0, []], (4, 7): [None, None, 0, []],
                  (5, 0): [None, None, 0, []], (5, 1): [None, None, 0, []], (5, 2): [None, None, 0, []], (5, 3): [None, None, 0, []], (5, 4): [None, None, 0, []],
                  (5, 5): [None, None, 0, []], (5, 6): [None, None, 0, []], (5, 7): [None, None, 0, []],
                  (6, 0): [pawn_white_1, white_pawn_image, 1, []], (6, 1): [pawn_white_2, white_pawn_image, 1, []],
                  (6, 2): [pawn_white_3, white_pawn_image, 1, []], (6, 3): [pawn_white_4, white_pawn_image, 1, []],
                  (6, 4): [pawn_white_5, white_pawn_image, 1, []], (6, 5): [pawn_white_6, white_pawn_image, 1, []],
                  (6, 6): [pawn_white_7, white_pawn_image, 1, []], (6, 7): [pawn_white_8, white_pawn_image, 1, []],
                  (7, 0): [rook_white_1, white_rook_image, 1, []], (7, 1): [knight_white_1, white_knight_image, 1, []],
                  (7, 2): [bishop_white_1, white_bishop_image, 1, []], (7, 3): [queen_white, white_queen_image, 1, []],
                  (7, 4): [king_white, white_king_image, 2, []], (7, 5): [bishop_white_2, white_bishop_image, 1, []],
                  (7, 6): [knight_white_2, white_knight_image, 1, []], (7, 7): [rook_white_2, white_rook_image, 1, []]}
    return dico_board


rook_white_1, rook_white_2, rook_black_1, rook_black_2,\
bishop_white_1, bishop_white_2, bishop_black_1, bishop_black_2,\
queen_white, queen_black, king_white, king_black, knight_white_1,\
knight_white_2, knight_black_1, knight_black_2, pawn_white_1, pawn_white_2,\
pawn_white_3, pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8,\
pawn_black_1, pawn_black_2, pawn_black_3, pawn_black_4, pawn_black_5, pawn_black_6,\
pawn_black_7, pawn_black_8 = create_pieces()

dico_board = create_dico_board()

LIST_BLACK_PIECES = [rook_black_1, rook_black_2, bishop_black_1, bishop_black_2, queen_black,
                     king_black, knight_black_1, knight_black_2, pawn_black_1, pawn_black_2, pawn_black_3,
                     pawn_black_4, pawn_black_5, pawn_black_6, pawn_black_7, pawn_black_8]

LIST_WHITE_PIECES = [rook_white_1, rook_white_2, bishop_white_1, bishop_white_2, king_white,
                     queen_white, knight_white_1, knight_white_2, pawn_white_1, pawn_white_2, pawn_white_3,
                     pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8]