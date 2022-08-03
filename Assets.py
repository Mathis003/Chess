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

def create_pieces():
    """ Create all the pieces objects"""
    from all_pieces import Rook, Bishop, Knight, Queen, King, Pawn # Import all the pieces
    """Initialize all the pieces objects"""
    # Rook
    rook_white_1 = Rook(white_rook_rect, [7, 0], -1)
    rook_white_2 = Rook(white_rook_rect, [7, 7], -1)
    rook_black_1 = Rook(black_rook_rect, [0, 0], 1)
    rook_black_2 = Rook(black_rook_rect, [0, 7], 1)
    # Bishop
    bishop_white_1 = Bishop(white_bishop_rect, [7, 2], -1)
    bishop_white_2 = Bishop(white_bishop_rect, [7, 5], -1)
    bishop_black_1 = Bishop(black_bishop_rect, [0, 2], 1)
    bishop_black_2 = Bishop(black_bishop_rect, [0, 5], 1)
    # Queen
    queen_white = Queen(white_queen_rect, [7, 3], -1)
    queen_black = Queen(black_queen_rect, [0, 3], 1)
    # King
    king_white = King(white_king_rect, [7, 4], -1)
    king_black = King(black_king_rect, [0, 4], 1)
    # Knight
    knight_white_1 = Knight(white_knight_rect, [7, 1], -1)
    knight_white_2 = Knight(white_knight_rect, [7, 6], -1)
    knight_black_1 = Knight(black_knight_rect, [0, 1], 1)
    knight_black_2 = Knight(black_knight_rect, [0, 6], 1)
    # Pawn
    pawn_white_1 = Pawn(white_pawn_rect, [6, 0], -1, True)
    pawn_white_2 = Pawn(white_pawn_rect, [6, 1], -1, True)
    pawn_white_3 = Pawn(white_pawn_rect, [6, 2], -1, True)
    pawn_white_4 = Pawn(white_pawn_rect, [6, 3], -1, True)
    pawn_white_5 = Pawn(white_pawn_rect, [6, 4], -1, True)
    pawn_white_6 = Pawn(white_pawn_rect, [6, 5], -1, True)
    pawn_white_7 = Pawn(white_pawn_rect, [6, 6], -1, True)
    pawn_white_8 = Pawn(white_pawn_rect, [6, 7], -1, True)
    pawn_black_1 = Pawn(black_pawn_rect, [1, 0], 1, True)
    pawn_black_2 = Pawn(black_pawn_rect, [1, 1], 1, True)
    pawn_black_3 = Pawn(black_pawn_rect, [1, 2], 1, True)
    pawn_black_4 = Pawn(black_pawn_rect, [1, 3], 1, True)
    pawn_black_5 = Pawn(black_pawn_rect, [1, 4], 1, True)
    pawn_black_6 = Pawn(black_pawn_rect, [1, 5], 1, True)
    pawn_black_7 = Pawn(black_pawn_rect, [1, 6], 1, True)
    pawn_black_8 = Pawn(black_pawn_rect, [1, 7], 1, True)

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

# Usefull to update the board (draw the pieces on the board) => know directly where the pieces are on the board.
dico_pieces = {rook_black_1 : [(0,0), black_rook_image], rook_black_2 : [(0,7), black_rook_image], bishop_black_1 : [(0, 2), black_bishop_image],
               bishop_black_2 : [(0, 5), black_bishop_image], knight_black_1 : [(0,1), black_knight_image], knight_black_2 : [(0,6), black_knight_image],
               king_black : [(0,4), black_king_image], queen_black : [(0,3), black_queen_image], pawn_black_1 : [(1,0), black_pawn_image], pawn_black_2 : [(1,1), black_pawn_image],
               pawn_black_3 : [(1,2), black_pawn_image], pawn_black_4 : [(1,3), black_pawn_image], pawn_black_5 : [(1,4), black_pawn_image], pawn_black_6 : [(1,5), black_pawn_image],
               pawn_black_7 : [(1,6), black_pawn_image], pawn_black_8 : [(1,7), black_pawn_image], pawn_white_1 : [(6,0), white_pawn_image], pawn_white_2 : [(6,1), white_pawn_image],
               pawn_white_3 : [(6,2), white_pawn_image], pawn_white_4 : [(6,3), white_pawn_image], pawn_white_5 : [(6,4), white_pawn_image], pawn_white_6 : [(6,5), white_pawn_image],
               pawn_white_7 : [(6,6), white_pawn_image], pawn_white_8 : [(6,7), white_pawn_image], rook_white_1 : [(7,0), white_rook_image], rook_white_2 : [(7,7), white_rook_image],
               bishop_white_1 : [(7, 2), white_bishop_image], bishop_white_2 : [(7, 5), white_bishop_image], knight_white_1 : [(7,1), white_knight_image], knight_white_2 : [(7,6), white_knight_image],
               king_white : [(7,4), white_king_image], queen_white : [(7,3), white_queen_image]}

# List of all the pieces objects => allow to access to all the pieces objects without testing all the board's tile.
# => will be update if the board is updated. (piece eaten, promotion, ...)
LIST_BLACK_PIECES = [rook_black_1, rook_black_2, bishop_black_1, bishop_black_2, queen_black,
                     king_black, knight_black_1, knight_black_2, pawn_black_1, pawn_black_2, pawn_black_3,
                     pawn_black_4, pawn_black_5, pawn_black_6, pawn_black_7, pawn_black_8]

LIST_WHITE_PIECES = [rook_white_1, rook_white_2, bishop_white_1, bishop_white_2, king_white,
                     queen_white, knight_white_1, knight_white_2, pawn_white_1, pawn_white_2, pawn_white_3,
                     pawn_white_4, pawn_white_5, pawn_white_6, pawn_white_7, pawn_white_8]