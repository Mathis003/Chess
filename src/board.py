from src.all_pieces import *
from src.all_configs.assets import *

class Board:
    
    def __init__(self, screen):
        self.screen = screen
    
    def change_image(self, idx_image):
        new_idx_image = abs(1 - idx_image)

        for piece in dico_list_pieces[1]:
            if isinstance(piece, type(Pawn((7, 4), 1, True))):
                dico_board[piece.tile][1] = white_pawn_image[new_idx_image]
            elif isinstance(piece, type(Queen((7, 4), 1, True))):
                dico_board[piece.tile][1] = white_queen_image[new_idx_image]
            elif isinstance(piece, type(King((7, 4), 1, True, 0, 0))):
                dico_board[piece.tile][1] = white_king_image[new_idx_image]
            elif isinstance(piece, type(Bishop((7, 4), 1, True))):
                dico_board[piece.tile][1] = white_bishop_image[new_idx_image]
            elif isinstance(piece, type(Knight((7, 4), 1, True))):
                dico_board[piece.tile][1] = white_knight_image[new_idx_image]
            elif isinstance(piece, type(Rook((7, 4), 1, True))):
                dico_board[piece.tile][1] = white_rook_image[new_idx_image]

        for piece in dico_list_pieces[-1]:
            if isinstance(piece, type(Pawn((7, 4), 1, True))):
                dico_board[piece.tile][1] = black_pawn_image[new_idx_image]
            elif isinstance(piece, type(Queen((7, 4), 1, True))):
                dico_board[piece.tile][1] = black_queen_image[new_idx_image]
            elif isinstance(piece, type(King((7, 4), 1, True, 0, 0))):
                dico_board[piece.tile][1] = black_king_image[new_idx_image]
            elif isinstance(piece, type(Bishop((7, 4), 1, True))):
                dico_board[piece.tile][1] = black_bishop_image[new_idx_image]
            elif isinstance(piece, type(Knight((7, 4), 1, True))):
                dico_board[piece.tile][1] = black_knight_image[new_idx_image]
            elif isinstance(piece, type(Rook((7, 4), 1, True))):
                dico_board[piece.tile][1] = black_rook_image[new_idx_image]

    def draw_tile(self, tile, color):
        """
        Draw the rect of a tile with the good color
        param tile: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number
        param color: new color of the tile
        """
        pygame.draw.rect(self.screen, color, (tile[1] * SIZE_SQUARE, tile[0] * SIZE_SQUARE, SIZE_SQUARE, SIZE_SQUARE))
    
    def check_dark_tile(self, tile):
        """
        Check if the tile is a dark tile or a light tile.
        param tile: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number
        """
        if tile[0] % 2 == 0:
            return (tile[1] % 2 != 0)
        else:
            return (tile[1] % 2 == 0)

    def draw_board(self, mod_board):
        """
        Draw all the board's tiles
        param mod_board: mod of the board's color
        """
        for i in range(ROW):
            for j in range(COL):
                if self.check_dark_tile((i, j)):
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][1])
                else:
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][0])

    def draw_pieces(self):
        """
        Draw all the pieces on the board.
        """
        for piece in LIST_WHITE_PIECES + LIST_BLACK_PIECES:
            # If the piece isn't pressed on the board => otherwise the image is None => = "Don't draw it"
            if dico_board[piece.tile][1] != None:
                self.screen.blit(dico_board[piece.tile][1], (piece.tile[1] * SIZE_SQUARE, piece.tile[0] * SIZE_SQUARE))
    
    def draw_possible_moves(self, tile_piece):
        """
        Draw the tile's new color of the pieces's all possible moves.
        param tile_piece: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number (where the piece is)
        """
        if tile_piece != (-1, -1):
            for move_tile in dico_board[tile_piece][3]:
                if self.check_dark_tile(move_tile):
                    self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_DARK)
                else:
                    self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_LIGHT)