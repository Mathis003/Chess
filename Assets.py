import numpy
import pygame
from Configs import *

"""Asset Class for all images"""
class Asset:
    """ Represent the image in the game """
    def __init__(self,link_image, dimension):
        self.link_image = link_image
        self.dimension = dimension

    def load_image(self):
        image = pygame.image.load(self.link_image)
        image = pygame.transform.scale(image, self.dimension)
        return image

# Load all the assets

# Black pieces
black_king_image = Asset("Pieces_image/bK.png", (SQUARE, SQUARE)).load_image()
black_queen_image = Asset("Pieces_image/bQ.png", (SQUARE, SQUARE)).load_image()
black_rook_image = Asset("Pieces_image/bR.png", (SQUARE, SQUARE)).load_image()
black_bishop_image = Asset("Pieces_image/bB.png", (SQUARE, SQUARE)).load_image()
black_knight_image = Asset("Pieces_image/bKN.png", (SQUARE, SQUARE)).load_image()
black_pawn_image = Asset("Pieces_image/bP.png", (SQUARE, SQUARE)).load_image()

# White pieces
white_king_image = Asset("Pieces_image/wK.png", (SQUARE, SQUARE)).load_image()
white_queen_image = Asset("Pieces_image/wQ.png", (SQUARE, SQUARE)).load_image()
white_rook_image = Asset("Pieces_image/wR.png", (SQUARE, SQUARE)).load_image()
white_bishop_image = Asset("Pieces_image/wB.png", (SQUARE, SQUARE)).load_image()
white_knight_image = Asset("Pieces_image/wKN.png", (SQUARE, SQUARE)).load_image()
white_pawn_image = Asset("Pieces_image/wP.png", (SQUARE, SQUARE)).load_image()

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
pygame.display.set_icon(black_king_image)

def create_pieces():
    """ Create all the pieces objects"""
    from all_pieces import Rook, Bishop, Knight, Queen, King, Pawn # Import all the pieces
    """Initialize all the pieces objects"""
    # Rook
    rook_white_1 = Rook((7, 0), 1, True)
    rook_white_2 = Rook((7, 7), 1, True)
    rook_black_1 = Rook((0, 0), -1, True)
    rook_black_2 = Rook((0, 7), -1, True)
    # Bishop
    bishop_white_1 = Bishop((7, 2), 1, True)
    bishop_white_2 = Bishop((7, 5), 1, True)
    bishop_black_1 = Bishop((0, 2), -1, True)
    bishop_black_2 = Bishop((0, 5), -1, True)
    # Queen
    queen_white = Queen((7, 3), 1, True)
    queen_black = Queen((0, 3), -1, True)
    # King
    king_white = King((7, 4), 1, True, rook_white_1, rook_white_2)
    king_black = King((0, 4), -1, True, rook_black_1, rook_black_2)
    # Knight
    knight_white_1 = Knight((7, 1), 1, True)
    knight_white_2 = Knight((7, 6), 1, True)
    knight_black_1 = Knight((0, 1), -1, True)
    knight_black_2 = Knight((0, 6), -1, True)
    # Pawn
    pawn_white_1 = Pawn((6, 0), 1, True)
    pawn_white_2 = Pawn((6, 1), 1, True)
    pawn_white_3 = Pawn((6, 2), 1, True)
    pawn_white_4 = Pawn((6, 3), 1, True)
    pawn_white_5 = Pawn((6, 4), 1, True)
    pawn_white_6 = Pawn((6, 5), 1, True)
    pawn_white_7 = Pawn((6, 6), 1, True)
    pawn_white_8 = Pawn((6, 7), 1, True)
    pawn_black_1 = Pawn((1, 0), -1, True)
    pawn_black_2 = Pawn((1, 1), -1, True)
    pawn_black_3 = Pawn((1, 2), -1, True)
    pawn_black_4 = Pawn((1, 3), -1, True)
    pawn_black_5 = Pawn((1, 4), -1, True)
    pawn_black_6 = Pawn((1, 5), -1, True)
    pawn_black_7 = Pawn((1, 6), -1, True)
    pawn_black_8 = Pawn((1, 7), -1, True)

    # Return all the pieces objects
    return rook_white_1, rook_white_2, rook_black_1, rook_black_2,\
           bishop_white_1, bishop_white_2, bishop_black_1, bishop_black_2,\
           queen_white, queen_black, king_white, king_black, knight_white_1,\
           knight_white_2, knight_black_1, knight_black_2, pawn_white_1,\
           pawn_white_2, pawn_white_3, pawn_white_4, pawn_white_5, pawn_white_6,\
           pawn_white_7, pawn_white_8, pawn_black_1, pawn_black_2, pawn_black_3,\
           pawn_black_4, pawn_black_5, pawn_black_6, pawn_black_7, pawn_black_8


def create_dico_board():
    """ Create the board dictionary"""

    """
    Dictionnary :
        key : tile's coordinates in a tuple (x, y)
        value : list with : object (piece), image_of_the_piece, number_of_the_piece, list_of_possibile_moves
        => number_of_the_piece : 0 if no piece, 1 if white piece, 2 if white king, -1 if black piece and -2 if black king
    """

    dico_board = {(0, 0): [rook_black_1, black_rook_image, -1, []],
                  (0, 1): [knight_black_1, black_knight_image, -1, [(2, 0), (2, 2)]],
                  (0, 2): [bishop_black_1, black_bishop_image, -1, []],
                  (0, 3): [queen_black, black_queen_image, -1, []], (0, 4): [king_black, black_king_image, -1, []],
                  (0, 5): [bishop_black_2, black_bishop_image, -1, []],
                  (0, 6): [knight_black_2, black_knight_image, -1, [(2, 5), (2, 7)]],
                  (0, 7): [rook_black_2, black_rook_image, -1, []],
                  (1, 0): [pawn_black_1, black_pawn_image, -1, [(2, 0), (3, 0)]], (1, 1): [pawn_black_2, black_pawn_image, -1, [(2, 1), (3, 1)]],
                  (1, 2): [pawn_black_3, black_pawn_image, -1, [(2, 2), (3, 2)]], (1, 3): [pawn_black_4, black_pawn_image, -1, [(2, 3), (3, 3)]],
                  (1, 4): [pawn_black_5, black_pawn_image, -1, [(2, 4), (3, 4)]], (1, 5): [pawn_black_6, black_pawn_image, -1, [(2, 5), (3, 5)]],
                  (1, 6): [pawn_black_7, black_pawn_image, -1, [(2, 6), (3, 6)]], (1, 7): [pawn_black_8, black_pawn_image, -1, [(2, 7), (3, 7)]],
                  (2, 0): [None, None, 0, []], (2, 1): [None, None, 0, []], (2, 2): [None, None, 0, []], (2, 3): [None, None, 0, []], (2, 4): [None, None, 0, []],
                  (2, 5): [None, None, 0, []], (2, 6): [None, None, 0, []], (2, 7): [None, None, 0, []],
                  (3, 0): [None, None, 0, []], (3, 1): [None, None, 0, []], (3, 2): [None, None, 0, []], (3, 3): [None, None, 0, []], (3, 4): [None, None, 0, []],
                  (3, 5): [None, None, 0, []], (3, 6): [None, None, 0, []], (3, 7): [None, None, 0, []],
                  (4, 0): [None, None, 0, []], (4, 1): [None, None, 0, []], (4, 2): [None, None, 0, []], (4, 3): [None, None, 0, []], (4, 4): [None, None, 0, []],
                  (4, 5): [None, None, 0, []], (4, 6): [None, None, 0, []], (4, 7): [None, None, 0, []],
                  (5, 0): [None, None, 0, []], (5, 1): [None, None, 0, []], (5, 2): [None, None, 0, []], (5, 3): [None, None, 0, []], (5, 4): [None, None, 0, []],
                  (5, 5): [None, None, 0, []], (5, 6): [None, None, 0, []], (5, 7): [None, None, 0, []],
                  (6, 0): [pawn_white_1, white_pawn_image, 1, [(5, 0), (4, 0)]], (6, 1): [pawn_white_2, white_pawn_image, 1, [(5, 1), (4, 1)]],
                  (6, 2): [pawn_white_3, white_pawn_image, 1, [(5, 2), (4, 2)]], (6, 3): [pawn_white_4, white_pawn_image, 1, [(5, 3), (4, 3)]],
                  (6, 4): [pawn_white_5, white_pawn_image, 1, [(5, 4), (4, 4)]], (6, 5): [pawn_white_6, white_pawn_image, 1, [(5, 5), (4, 5)]],
                  (6, 6): [pawn_white_7, white_pawn_image, 1, [(5, 6), (4, 6)]], (6, 7): [pawn_white_8, white_pawn_image, 1, [(5, 7), (4, 7)]],
                  (7, 0): [rook_white_1, white_rook_image, 1, []], (7, 1): [knight_white_1, white_knight_image, 1, [(5, 0), (5, 2)]],
                  (7, 2): [bishop_white_1, white_bishop_image, 1, []], (7, 3): [queen_white, white_queen_image, 1, []],
                  (7, 4): [king_white, white_king_image, 1, []], (7, 5): [bishop_white_2, white_bishop_image, 1, []],
                  (7, 6): [knight_white_2, white_knight_image, 1, [(5, 5), (5, 7)]], (7, 7): [rook_white_2, white_rook_image, 1, []]}

    # Return the dictionary
    return dico_board

# Call the function to create all the pieces objects (need function otherwise a circular import dependencies are made).
rook_white_1, rook_white_2, rook_black_1, rook_black_2,\
bishop_white_1, bishop_white_2, bishop_black_1, bishop_black_2,\
queen_white, queen_black, king_white, king_black, knight_white_1,\
knight_white_2, knight_black_1, knight_black_2, pawn_white_1, pawn_white_2,\
pawn_white_3, pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8,\
pawn_black_1, pawn_black_2, pawn_black_3, pawn_black_4, pawn_black_5, pawn_black_6,\
pawn_black_7, pawn_black_8 = create_pieces()

# Call the function to create the dico of the board (need function otherwise a circular import dependencies are made).
# => will be update every turn.
# Useful if we know the tile and we want the information about the piece on it.
dico_board = create_dico_board()

# List of all the pieces objects => allow to access to all the pieces objects without testing all the board's tile.
# => will be update if the board is updated. (piece eaten, promotion, ...)
LIST_BLACK_PIECES = [rook_black_1, rook_black_2, bishop_black_1, bishop_black_2, queen_black,
                     king_black, knight_black_1, knight_black_2, pawn_black_1, pawn_black_2, pawn_black_3,
                     pawn_black_4, pawn_black_5, pawn_black_6, pawn_black_7, pawn_black_8]

LIST_WHITE_PIECES = [rook_white_1, rook_white_2, bishop_white_1, bishop_white_2, king_white,
                     queen_white, knight_white_1, knight_white_2, pawn_white_1, pawn_white_2, pawn_white_3,
                     pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8]

matrix_points_pawn_white = [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

matrix_points_pawn_black = list(numpy.array(matrix_points_pawn_white)[::-1]) # Reverse the matrix

matrix_points_knight_white = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]
matrix_points_knight_black = matrix_points_knight_white

matrix_points_bishop_white = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

matrix_points_bishop_black = list(numpy.array(matrix_points_bishop_white)[::-1]) # Reverse the matrix

matrix_points_rook_white = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

matrix_points_rook_black = list(numpy.array(matrix_points_rook_white)[::-1]) # Reverse the matrix

matrix_points_queen_white = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

matrix_points_queen_black = matrix_points_queen_white

matrix_points_king_white = [

    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

matrix_points_king_black = list(numpy.array(matrix_points_king_white)[::-1]) # Reverse the matrix