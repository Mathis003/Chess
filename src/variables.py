from src.all_pieces import Rook, Queen, King, Pawn, Bishop, Knight

"""
Variables used in almost every file .py
"""

rook_white_left = Rook((7, 0), 1)
rook_white_right = Rook((7, 7), 1)
rook_black_left = Rook((0, 0), -1)
rook_black_right = Rook((0, 7), -1)

board_pieces = [[rook_black_left, Knight((0, 1), -1), Bishop((0, 2), -1), Queen((0, 3), -1), King((0, 4), -1, rook_black_left, rook_black_right), Bishop((0, 5), -1), Knight((0, 6), -1), rook_black_right],
                [Pawn((1, 0), -1), Pawn((1, 1), -1), Pawn((1, 2), -1), Pawn((1, 3), -1), Pawn((1, 4), -1), Pawn((1, 5), -1), Pawn((1, 6), -1), Pawn((1, 7), -1)],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Pawn((6, 0), 1), Pawn((6, 1), 1), Pawn((6, 2), 1), Pawn((6, 3), 1), Pawn((6, 4), 1), Pawn((6, 5), 1), Pawn((6, 6), 1), Pawn((6, 7), 1)],
                [rook_white_left, Knight((7, 1), 1), Bishop((7, 2), 1), Queen((7, 3), 1), King((7, 4), 1, rook_white_left, rook_white_right), Bishop((7, 5), 1), Knight((7, 6), 1), rook_white_right]]

list_black_pieces = []
for i in range(0, 2):
    for j in range(8):
        list_black_pieces.append(board_pieces[i][j])

list_white_pieces = []
for i in range(6, 8):
    for j in range(8):
        list_white_pieces.append(board_pieces[i][j])