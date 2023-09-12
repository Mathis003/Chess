from src.all_configs.assets import *
from src.all_pieces import Rook, Bishop, Knight, Queen, King, Pawn


### File that contain important variables ###
### dico_board | LIST_WHITE_PIECES | LIST_BLACK_PIECES | ico_list_pieces ###


"""
Initialize all the pieces instances ###
"""
# Rook
rook_white = [Rook((7, 0), 1, True), Rook((7, 7), 1, True)]
rook_black = [Rook((0, 0), -1, True), Rook((0, 7), -1, True)]

# Bishop
bishop_white = [Bishop((7, 2), 1, True), Bishop((7, 5), 1, True)]
bishop_black = [Bishop((0, 2), -1, True), Bishop((0, 5), -1, True)]

# Queen
queen_white = Queen((7, 3), 1, True)
queen_black = Queen((0, 3), -1, True)

# King
king_white = King((7, 4), 1, True, rook_white[0], rook_white[1])
king_black = King((0, 4), -1, True, rook_black[0], rook_black[1])

# Knight
knight_white = [Knight((7, 1), 1, True), Knight((7, 6), 1, True)]
knight_black = [Knight((0, 1), -1, True), Knight((0, 6), -1, True)]

# Pawn
pawn_white = [Pawn((6, 0), 1, True), Pawn((6, 1), 1, True), Pawn((6, 2), 1, True), Pawn((6, 3), 1, True),
              Pawn((6, 4), 1, True), Pawn((6, 5), 1, True), Pawn((6, 6), 1, True), Pawn((6, 7), 1, True)]

pawn_black = [Pawn((1, 0), -1, True), Pawn((1, 1), -1, True), Pawn((1, 2), -1, True), Pawn((1, 3), -1, True),
              Pawn((1, 4), -1, True), Pawn((1, 5), -1, True), Pawn((1, 6), -1, True), Pawn((1, 7), -1, True)]


"""
Create the dico of the board => will be update every turn.
Useful if we know the tile and we want the information about the piece on it.

Dictionnary :
    key : tile's coordinates in a tuple (x, y)
    value : list with : object (piece), image_of_the_piece, number_of_the_piece, list_of_possibile_moves
    => number_of_the_piece : 0 if no piece, 1 if white piece, 2 if white king, -1 if black piece
"""
dico_board = {(0, 0): [rook_black[0], black_rook_image[0], -1, []],
            (0, 1): [knight_black[0], black_knight_image[0], -1, [(2, 0), (2, 2)]],
            (0, 2): [bishop_black[0], black_bishop_image[0], -1, []],
            (0, 3): [queen_black, black_queen_image[0], -1, []], (0, 4): [king_black, black_king_image[0], -1, []],
            (0, 5): [bishop_black[1], black_bishop_image[0], -1, []],
            (0, 6): [knight_black[1], black_knight_image[0], -1, [(2, 5), (2, 7)]],
            (0, 7): [rook_black[1], black_rook_image[0], -1, []],
            (1, 0): [pawn_black[0], black_pawn_image[0], -1, [(2, 0), (3, 0)]], (1, 1): [pawn_black[1], black_pawn_image[0], -1, [(2, 1), (3, 1)]],
            (1, 2): [pawn_black[2], black_pawn_image[0], -1, [(2, 2), (3, 2)]], (1, 3): [pawn_black[3], black_pawn_image[0], -1, [(2, 3), (3, 3)]],
            (1, 4): [pawn_black[4], black_pawn_image[0], -1, [(2, 4), (3, 4)]], (1, 5): [pawn_black[5], black_pawn_image[0], -1, [(2, 5), (3, 5)]],
            (1, 6): [pawn_black[6], black_pawn_image[0], -1, [(2, 6), (3, 6)]], (1, 7): [pawn_black[7], black_pawn_image[0], -1, [(2, 7), (3, 7)]],
            (2, 0): [None, None, 0, []], (2, 1): [None, None, 0, []], (2, 2): [None, None, 0, []], (2, 3): [None, None, 0, []], (2, 4): [None, None, 0, []],
            (2, 5): [None, None, 0, []], (2, 6): [None, None, 0, []], (2, 7): [None, None, 0, []],
            (3, 0): [None, None, 0, []], (3, 1): [None, None, 0, []], (3, 2): [None, None, 0, []], (3, 3): [None, None, 0, []], (3, 4): [None, None, 0, []],
            (3, 5): [None, None, 0, []], (3, 6): [None, None, 0, []], (3, 7): [None, None, 0, []],
            (4, 0): [None, None, 0, []], (4, 1): [None, None, 0, []], (4, 2): [None, None, 0, []], (4, 3): [None, None, 0, []], (4, 4): [None, None, 0, []],
            (4, 5): [None, None, 0, []], (4, 6): [None, None, 0, []], (4, 7): [None, None, 0, []],
            (5, 0): [None, None, 0, []], (5, 1): [None, None, 0, []], (5, 2): [None, None, 0, []], (5, 3): [None, None, 0, []], (5, 4): [None, None, 0, []],
            (5, 5): [None, None, 0, []], (5, 6): [None, None, 0, []], (5, 7): [None, None, 0, []],
            (6, 0): [pawn_white[0], white_pawn_image[0], 1, [(5, 0), (4, 0)]], (6, 1): [pawn_white[1], white_pawn_image[0], 1, [(5, 1), (4, 1)]],
            (6, 2): [pawn_white[2], white_pawn_image[0], 1, [(5, 2), (4, 2)]], (6, 3): [pawn_white[3], white_pawn_image[0], 1, [(5, 3), (4, 3)]],
            (6, 4): [pawn_white[4], white_pawn_image[0], 1, [(5, 4), (4, 4)]], (6, 5): [pawn_white[5], white_pawn_image[0], 1, [(5, 5), (4, 5)]],
            (6, 6): [pawn_white[6], white_pawn_image[0], 1, [(5, 6), (4, 6)]], (6, 7): [pawn_white[7], white_pawn_image[0], 1, [(5, 7), (4, 7)]],
            (7, 0): [rook_white[0], white_rook_image[0], 1, []], (7, 1): [knight_white[0], white_knight_image[0], 1, [(5, 0), (5, 2)]],
            (7, 2): [bishop_white[0], white_bishop_image[0], 1, []], (7, 3): [queen_white, white_queen_image[0], 1, []],
            (7, 4): [king_white, white_king_image[0], 1, []], (7, 5): [bishop_white[1], white_bishop_image[0], 1, []],
            (7, 6): [knight_white[1], white_knight_image[0], 1, [(5, 5), (5, 7)]], (7, 7): [rook_white[1], white_rook_image[0], 1, []]}


"""
List of all the pieces objects => allow to access to all the pieces objects without testing all the board's tile.
=> will be update if the board is updated. (piece eaten, promotion,...).
"""
LIST_BLACK_PIECES = [rook_black[0], rook_black[1], bishop_black[0], bishop_black[1], queen_black,
                     king_black, knight_black[0], knight_black[1], pawn_black[0], pawn_black[1], pawn_black[2],
                     pawn_black[3], pawn_black[4], pawn_black[5], pawn_black[6], pawn_black[7]]

LIST_WHITE_PIECES = [rook_white[0], rook_white[1], bishop_white[0], bishop_white[1], king_white,
                     queen_white, knight_white[0], knight_white[1], pawn_white[0], pawn_white[1], pawn_white[2],
                     pawn_white[3], pawn_white[4], pawn_white[5], pawn_white[6], pawn_white[7]]

dico_list_pieces = {1 : LIST_WHITE_PIECES, -1 : LIST_BLACK_PIECES}