from src.assets import *
from src.all_pieces import Rook, King, Queen, Pawn, Bishop, Knight


## TODO :METTRE self.board_pieces, self.list_black_pieces, self.list_white_pieces AUTRE PART !!
## TODO :METTRE self.board_pieces, self.list_black_pieces, self.list_white_pieces AUTRE PART !!
## TODO :METTRE self.board_pieces, self.list_black_pieces, self.list_white_pieces AUTRE PART !!

class Board:
    
    def __init__(self, screen):
        self.screen = screen

        self.rook_white_left = Rook(None, [], [], (7, 0), 1, [], white_rook_image, 0, True)
        self.rook_white_right = Rook(None, [], [], (7, 7), 1, [], white_rook_image, 0, True)
        self.rook_black_left = Rook(None, [], [], (0, 0), -1, [], black_rook_image, 0, True)
        self.rook_black_right = Rook(None, [], [], (0, 7), -1, [], black_rook_image, 0,True)

        self.board_pieces = [[self.rook_black_left, Knight(None, [], [], (0, 1), -1, [(2, 0), (2, 2)], black_knight_image, 0, True), Bishop(None, [], [], (0, 2), -1, [], black_bishop_image, 0, True), Queen(None, [], [], (0, 3), -1, [], black_queen_image, 0, True), King(None, [], [], (0, 4), -1, [], black_king_image, 0, True,  self.rook_black_left,  self.rook_black_right), Bishop(None, [], [], (0, 5), -1, [], black_bishop_image, 0,True), Knight(None, [], [], (0, 6), -1, [(2, 5), (2, 7)], black_knight_image, 0, True),  self.rook_black_right],
                            [Pawn(None, [], [], (1, 0), -1, [(2, 0), (3, 0)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 1), -1, [(2, 1), (3, 1)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 2), -1, [(2, 2), (3, 2)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 3), -1, [(2, 3), (3, 3)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 4), -1, [(2, 4), (3, 4)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 5), -1, [(2, 5), (3, 5)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 6), -1, [(2, 6), (3, 6)], black_pawn_image, 0, True), Pawn(None, [], [], (1, 7), -1, [(2, 7), (3, 7)], black_pawn_image, 0, True)],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [Pawn(None, [], [], (6, 0), 1, [(5, 0), (4, 0)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 1), 1, [(5, 1), (4, 1)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 2), 1, [(5, 2), (4, 2)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 3), 1, [(5, 3), (4, 3)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 4), 1, [(5, 4), (4, 4)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 5), 1, [(5, 5), (4, 5)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 6), 1, [(5, 6), (4, 6)], white_pawn_image, 0, True), Pawn(None, [], [], (6, 7), 1, [(5, 7), (4, 7)], white_pawn_image, 0, True)],
                            [self.rook_white_left, Knight(None, [], [], (7, 1), 1, [(5, 0), (5, 2)], white_knight_image, 0, True), Bishop(None, [], [], (7, 2), 1, [], white_bishop_image, 0, True), Queen(None, [], [], (7, 3), 1, [], white_queen_image, 0, True), King(None, [], [], (7, 4), 1, [], white_king_image, 0, True,  self.rook_white_left,  self.rook_white_right), Bishop(None, [], [], (7, 5), 1, [], white_bishop_image, 0, True), Knight(None, [], [], (7, 6), 1, [(5, 5), (5, 7)], white_knight_image, 0, True),  self.rook_white_right]]

        self.list_black_pieces = []
        for i in range(0, 2):
            for j in range(8):
                self.list_black_pieces.append(self.board_pieces[i][j])

        self.list_white_pieces = []
        for i in range(6, 8):
            for j in range(8):
                self.list_white_pieces.append(self.board_pieces[i][j])
        
    def change_image(self):
        for piece in self.dico_list_pieces[1]:
            piece.current_idx_image = abs(1 - piece.current_idx_image)

    def draw_tile(self, tile, color):
        pygame.draw.rect(self.screen, color, (tile[1] * SIZE_SQUARE, tile[0] * SIZE_SQUARE, SIZE_SQUARE, SIZE_SQUARE))
    
    def check_dark_tile(self, tile):
        if tile[0] % 2 == 0:
            return (tile[1] % 2 != 0)
        else:
            return (tile[1] % 2 == 0)

    def draw_board(self, mod_board):
        for i in range(ROW):
            for j in range(COL):
                if self.check_dark_tile((i, j)):
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][1])
                else:
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][0])
    
    def draw_possible_moves(self, available_moves):
        for move_tile in available_moves:
            if self.check_dark_tile(move_tile):
                self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_DARK)
            else:
                self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_LIGHT)