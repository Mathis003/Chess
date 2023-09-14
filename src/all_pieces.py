from src.assets import *
from src.piece import Piece


class Pawn(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)
        self.just_moved = False # Variable for the special stroke "En Passant"

    def update_possible_moves(self):
         
        self.available_moves = []

        # If the tile above the pawn is empty
        piece = self.board_pieces[self.tile[0] - self.color][self.tile[1]]
        if piece == None:
            self.available_moves.append((self.tile[0] - self.color, self.tile[1]))
            
            # If the pawn is on its first move and the tile above is empty
            if self.first_move:
                # If the tile above (x2) the pawn is empty (special stroke when first move)
                piece = self.board_pieces[self.tile[0] - 2 * self.color][self.tile[1]]
                if piece == None:
                    self.available_moves.append((self.tile[0] - 2 * self.color, self.tile[1]))

        # Attack moves
        for i in range(-1, 2, 2):
            if (0 <= self.tile[1] + i <= 7):
                # If the tile diagonally above the pawn is occupied by an opponent piece
                piece = self.board_pieces[self.tile[0] - self.color][self.tile[1] + i]
                if piece != None:
                    if piece.color == -self.color:
                        self.available_moves.append((self.tile[0] - self.color, self.tile[1] + i))

        self.move_en_passant()

    def move_en_passant(self):
        """
        Return a list with the possible "En Passant" move (max 2 possibility).
        """
        right_tile = (self.tile[0], self.tile[1] + 1)
        left_tile = (self.tile[0], self.tile[1] - 1)

        if (0 <= right_tile[1] <= 7):
            piece_right = self.board_pieces[right_tile[0]][right_tile[1]]
            # If the tile to the right is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if (type(piece_right) == type(self)) and piece_right.just_moved:
                self.available_moves.append((self.tile[0] - self.color, right_tile[1]))

        if (0 <= left_tile[1] <= 7):
            piece_left = self.board_pieces[left_tile[0]][left_tile[1]]
            # If the tile to the left is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if (type(piece_left) == type(self)) and piece_left.just_moved:
                self.available_moves.append((self.tile[0] - self.color, left_tile[1]))

    def move_piece(self, current_tile, new_tile, idx_image):

        # If the pawn can be promoted into a queen.
        if new_tile[0] == 0 or new_tile[0] == 7:
            mod_of_move = self.get_mod_move(new_tile)

            new_queen = Queen(self.board_pieces, self.list_black_pieces, self.list_white_pieces, new_tile, self.color, [], white_queen_image, idx_image, False)
            piece_eaten = self.board_pieces[new_tile[0]][new_tile[1]]
            if piece_eaten != None:
                self.remove_piece(piece_eaten)
            self.remove_piece(self.board_pieces[current_tile[0]][current_tile[1]])
            self.add_piece(new_queen)
            self.board_pieces[new_tile[0]][new_tile[1]] = new_queen
            return mod_of_move
        else:
            if (new_tile[0] == 3 or new_tile[0] == 4) and self.first_move:
                self.just_moved = True
                self.first_move = False
            else:
                self.just_moved = False
            
            # If the move is 'en passant'
            if (self.board_pieces[new_tile[0]][new_tile[1]] == None) and (new_tile[1] != current_tile[1]):
                piece_eaten = self.board_pieces[new_tile[0] + self.color][new_tile[1]]
                self.remove_piece(piece_eaten)
                self.board_pieces[new_tile[0] - self.color][new_tile[1]] = None

            return super().move_piece(current_tile, new_tile, idx_image)
        

        
class King(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move, rook_left, rook_right):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)
        self.rook_left = rook_left # Rook at the left of the king
        self.rook_right = rook_right # Rook at the right of the king

    def update_possible_moves(self):
         
        self.available_moves = []

        # All moves of the king (four diagonal, two sense in horizontal direction and two sense in vertical direction => 8 possibility if no tile is out of range)
        for i in range(-1, 2):
            for j in range(-1, 2):
                # If the tile is not the same as the king
                if (i, j) != (0,0) and ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] + j <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = self.board_pieces[self.tile[0] + i][self.tile[1] + j]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
    
        self.castling_stroke()

    def tiles_empty(self, list_tile):

        for tile in list_tile:
            if self.board_pieces[tile[0]][tile[1]] != None:
                return False
        return True

    def tiles_chess(self, list_tile):

        if self.color == 1:
            list_tile.append((7, 4))
        else:
            list_tile.append((0, 4))

        if self.color == 1:
            list_pieces = self.list_white_pieces
        else:
            list_pieces = self.list_black_pieces

        for piece in list_pieces:
            piece.update_possible_moves()
            for tile in list_tile:
                if tile in piece.available_moves:
                    return True
        return False
    
    def castling_aux(self, list_tiles_left, list_tiles_right, tiles_left_append, tiles_right_append):
         
        if self.first_move:
            if self.rook_left.first_move:
                # If the tiles between the king and the left rook are empty and not in check
                if self.tiles_empty(list_tiles_left) and not self.tiles_chess(list_tiles_left):
                    self.available_moves.append(tiles_left_append)

            # If the king and the right rook haven't played yet
            if self.rook_right.first_move:
                # If the tiles between the king and the right rook are empty and not in check
                if self.tiles_empty(list_tiles_right) and not self.tiles_chess(list_tiles_right):
                    self.available_moves.append(tiles_right_append)

    def castling_stroke(self):

        # color : [list_tile_left_stroke, list_tile_right_stroke, tile_to_append_left, tile_to_append_right]
        DICO_TILES = {1 : [[(7, 5), (7, 6)], [(7, 3), (7, 2), (7, 1)], (7, 6), (7, 2)],
                     -1 : [[(0, 5), (0, 6)], [(0, 3), (0, 2), (0, 1)], (0, 6), (0, 2)]}

        self.castling_aux(DICO_TILES[self.color][0], DICO_TILES[self.color][1], DICO_TILES[self.color][2], DICO_TILES[self.color][3])
    
    def move_piece(self, current_tile, new_tile, idx_image):

        if self.first_move:
            # Right castling
            if new_tile == (7, 6) or new_tile == (0, 6):
                self.board_pieces[new_tile[0]][6] = self.board_pieces[new_tile[0]][4]
                self.board_pieces[new_tile[0]][7] = None
                rook_piece = self.board_pieces[new_tile[0]][5]
                rook_piece.tile = (new_tile[0], 5)
                rook_piece.first_move = False
                self.first_move = False
                self.tile = new_tile
                return "castling"

            # Left castling
            elif new_tile == (7, 2) or new_tile == (0, 2):
                self.board_pieces[new_tile[0]][2] = self.board_pieces[new_tile[0]][4]
                self.board_pieces[new_tile[0]][0] = None
                rook_piece = self.board_pieces[new_tile[0]][3]
                rook_piece.tile = (new_tile[0], 3)
                rook_piece.first_move = False
                self.first_move = False
                self.tile = new_tile
                return "castling"
            else:
                self.first_move = False

        # Basic move
        return super().move_piece(current_tile, new_tile, idx_image)



class Knight(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):
         
        self.available_moves = []

        # All moves of the knight (two tiles in a direction and one tile in the perpendicular direction => in every sense => 8 possibility if no tile is out of range)
        for i in range(-2, 3, 4): # -2 or 2
            for j in range(-1, 2, 2): # -1 or 1
                if ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] + j <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = self.board_pieces[self.tile[0] + i][self.tile[1] + j]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))

                if ((0 <= self.tile[0] + j <= 7) and (0 <= self.tile[1] + i <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = self.board_pieces[self.tile[0] + j][self.tile[1] + i]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + j, self.tile[1] + i))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + j, self.tile[1] + i))



class Rook(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):
         
        self.available_moves = []

        UP_ENTER = True
        DOWN_ENTER = True  
        LEFT_ENTER = True
        RIGHT_ENTER = True

        # Vertical moves (Up)
        for i in range(1, self.tile[0] + 1):
            if UP_ENTER:
                # If the tile is empty
                piece = self.board_pieces[self.tile[0] - i][self.tile[1]]
                if piece == None:
                    self.available_moves.append((self.tile[0] - i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif piece.color == -self.color:
                    self.available_moves.append((self.tile[0] - i, self.tile[1]))
                    UP_ENTER = False
                else:
                    UP_ENTER = False
        
        # Vertical moves (Down)
        for i in  range(1, ROW - self.tile[0]):
            if DOWN_ENTER:
                # If the tile is empty
                piece = self.board_pieces[self.tile[0] + i][self.tile[1]]
                if piece == None:
                    self.available_moves.append((self.tile[0] + i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0] + i, self.tile[1]))  
                    DOWN_ENTER = False
                else:
                    DOWN_ENTER = False

        # Horizontal moves (Left)
        for i in range(1, self.tile[1] + 1):
            if LEFT_ENTER:
                # If the tile is empty
                piece = self.board_pieces[self.tile[0]][self.tile[1] - i]
                if piece == None:
                    self.available_moves.append((self.tile[0], self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0], self.tile[1] - i))   
                    LEFT_ENTER = False
                else:
                    LEFT_ENTER = False

        # Horizontal moves (Right)
        for i in range(1, COL - self.tile[1]):
            if RIGHT_ENTER:
                # If the tile is empty
                piece = self.board_pieces[self.tile[0]][self.tile[1] + i]
                if piece == None:
                    self.available_moves.append((self.tile[0], self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0], self.tile[1] + i))  
                    RIGHT_ENTER = False 
                else:
                    RIGHT_ENTER = False 



class Bishop(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):

        self.available_moves = []

        # Diagonal Left-Up
        for i in range(1, ROW):
            # If the tile is empty
            if ((0 <= self.tile[0] - i <= 7) and (0 <= self.tile[1] - i <= 7)):
                piece = self.board_pieces[self.tile[0] - i][self.tile[1] - i]
                if piece == None:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif self.board_pieces[self.tile[0] - i][self.tile[1] - i].color == - self.color:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] - i))   
                    break
                else:
                    break

        # Diagonal Left-Down
        for i in range(1, ROW):
            if ((0 <= self.tile[0] - i <= 7) and (0 <= self.tile[1] + i <= 7)):
                # If the tile is empty
                piece = self.board_pieces[self.tile[0] - i][self.tile[1] + i]
                if piece == None:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] + i))   
                    break
                else:
                    break

        # Diagonal Right-Up
        for i in range(1, ROW):
            if ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] - i <= 7)):
                # If the tile is empty
                piece = self.board_pieces[self.tile[0] + i][self.tile[1] - i]
                if piece == None:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] - i))   
                    break
                else:
                    break

        # Diagonal Right-Down
        for i in range(1, ROW):
            if ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] + i <= 7)):
                # If the tile is empty
                piece = self.board_pieces[self.tile[0] + i][self.tile[1] + i]
                if piece == None:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] + i))   
                    break
                else:
                    break



class Queen(Piece):

    def __init__(self, board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(board_pieces, list_black_piece, list_white_piece, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):

        bishop = Bishop(self.board_pieces, self.list_black_pieces, self.list_white_pieces, self.tile, self.color, [], [None, None], 0, self.first_move)
        bishop.update_possible_moves()

        rook = Rook(self.board_pieces, self.list_black_pieces, self.list_white_pieces, self.tile, self.color, [], [None, None], 0, self.first_move)
        rook.update_possible_moves()

        self.available_moves = (rook.available_moves + bishop.available_moves)

        bishop = None
        rook = None