from src.all_pieces import Rook, Queen, King, Pawn, Bishop, Knight
from src.assets import *

rook_white_left = Rook(None, [], [], (7, 0), 1, [], white_rook_image, 0, True)
rook_white_right = Rook(None, [], [], (7, 7), 1, [], white_rook_image, 0, True)
rook_black_left = Rook(None, [], [], (0, 0), -1, [], black_rook_image, 0, True)
rook_black_right = Rook(None, [], [], (0, 7), -1, [], black_rook_image, 0,True)

board_pieces = [[rook_black_left, Knight(None, [], [], (0, 1), -1, [(2, 0), (2, 2)], black_knight_image, 0, True), Bishop(None, [], [], (0, 2), -1, [], black_bishop_image, 0, True), Queen(None, [], [], (0, 3), -1, [], black_queen_image, 0, True), King(None, [], [], (0, 4), -1, [], black_king_image, 0, True,  rook_black_left,  rook_black_right), Bishop(None, [], [], (0, 5), -1, [], black_bishop_image, 0,True), Knight(None, [], [], (0, 6), -1, [(2, 5), (2, 7)], black_knight_image, 0, True),  rook_black_right],
                [Pawn(None, [], [], (1, 0), -1, [(2, 0), (3, 0)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 1), -1, [(2, 1), (3, 1)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 2), -1, [(2, 2), (3, 2)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 3), -1, [(2, 3), (3, 3)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 4), -1, [(2, 4), (3, 4)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 5), -1, [(2, 5), (3, 5)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 6), -1, [(2, 6), (3, 6)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 7), -1, [(2, 7), (3, 7)], black_pawn_image, 0, True)],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Pawn(None, [], [], (6, 0), 1, [(5, 0), (4, 0)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 1), 1, [(5, 1), (4, 1)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 2), 1, [(5, 2), (4, 2)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 3), 1, [(5, 3), (4, 3)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 4), 1, [(5, 4), (4, 4)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 5), 1, [(5, 5), (4, 5)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 6), 1, [(5, 6), (4, 6)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 7), 1, [(5, 7), (4, 7)], white_pawn_image, 0, True)],
                [rook_white_left, Knight(None, [], [], (7, 1), 1, [(5, 0), (5, 2)], white_knight_image, 0, True), Bishop(None, [], [], (7, 2), 1, [], white_bishop_image, 0, True), Queen(None, [], [], (7, 3), 1, [], white_queen_image, 0, True), King(None, [], [], (7, 4), 1, [], white_king_image, 0, True,  rook_white_left,  rook_white_right), Bishop(None, [], [], (7, 5), 1, [], white_bishop_image, 0, True), Knight(None, [], [], (7, 6), 1, [(5, 5), (5, 7)], white_knight_image, 0, True),  rook_white_right]]

list_black_pieces = []
for i in range(0, 2):
    for j in range(8):
        list_black_pieces.append(board_pieces[i][j])

list_white_pieces = []
for i in range(6, 8):
    for j in range(8):
        list_white_pieces.append(board_pieces[i][j])