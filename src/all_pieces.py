from src.piece import Piece
from src.configs import ROW, COL
from src.assets import white_pawn_image, black_pawn_image, white_queen_image, \
                       black_queen_image, white_king_image, black_king_image, \
                       white_knight_image, black_knight_image, white_rook_image, \
                       black_rook_image, white_bishop_image, black_bishop_image

class Pawn(Piece):

    def __init__(self, tile, color):

        self.tile = tile
        self.color = color

        self.list_image = [white_pawn_image, black_pawn_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

    def update_possible_moves(self):
         
        self.available_moves = []
        board_pieces = self.get_board_pieces()

        # If the tile above the pawn is empty
        piece = board_pieces[self.tile[0] - self.color][self.tile[1]]
        if piece == None:
            self.available_moves.append((self.tile[0] - self.color, self.tile[1]))
            
            # If the pawn is on its first move and the tile above is empty
            if self.first_move:
                # If the tile above (x2) the pawn is empty (special stroke when first move)
                piece = board_pieces[self.tile[0] - 2 * self.color][self.tile[1]]
                if piece == None:
                    self.available_moves.append((self.tile[0] - 2 * self.color, self.tile[1]))

        # Attack moves
        for i in range(-1, 2, 2):
            if (0 <= self.tile[1] + i <= 7):
                # If the tile diagonally above the pawn is occupied by an opponent piece
                piece = board_pieces[self.tile[0] - self.color][self.tile[1] + i]
                if piece != None:
                    if piece.color == -self.color:
                        self.available_moves.append((self.tile[0] - self.color, self.tile[1] + i))

        self.move_en_passant()

    def move_en_passant(self):

        board_pieces = self.get_board_pieces()

        right_tile = (self.tile[0], self.tile[1] + 1)
        left_tile = (self.tile[0], self.tile[1] - 1)

        if (0 <= right_tile[1] <= 7):
            piece_right = board_pieces[right_tile[0]][right_tile[1]]
            # If the tile to the right is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if (type(piece_right) == type(self)) and piece_right.just_moved:
                self.available_moves.append((self.tile[0] - self.color, right_tile[1]))

        if (0 <= left_tile[1] <= 7):
            piece_left = board_pieces[left_tile[0]][left_tile[1]]
            # If the tile to the left is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if (type(piece_left) == type(self)) and piece_left.just_moved:
                self.available_moves.append((self.tile[0] - self.color, left_tile[1]))

    def move_piece(self, current_tile, new_tile, idx_image):
        
        board_pieces = self.get_board_pieces()

        # If the pawn can be promoted into a queen.
        if new_tile[0] == 0 or new_tile[0] == 7:
            mod_of_move = self.get_mod_move(new_tile)

            new_queen = Queen(new_tile, self.color)
            new_queen.first_move = False

            if self.color == 1:
                image_queen = white_queen_image[idx_image]
            else:
                image_queen = black_queen_image[idx_image]
            
            new_queen.image = image_queen

            piece_eaten = board_pieces[new_tile[0]][new_tile[1]]
            if piece_eaten != None:
                self.remove_piece(piece_eaten)

            self.remove_piece(self)
            self.add_piece(new_queen)
            board_pieces[new_tile[0]][new_tile[1]] = new_queen
            board_pieces[current_tile[0]][current_tile[1]] = None
            return mod_of_move
        
        else:
            if (new_tile[0] == 3 or new_tile[0] == 4) and self.first_move:
                self.just_moved = True
                self.first_move = False
            else:
                self.just_moved = False
            
            # If the move is 'en passant'
            if (board_pieces[new_tile[0]][new_tile[1]] == None) and (new_tile[1] != current_tile[1]):
                piece_eaten = board_pieces[new_tile[0] + self.color][new_tile[1]]
                self.remove_piece(piece_eaten)
                board_pieces[new_tile[0] + self.color][new_tile[1]] = None

            return super().move_piece(current_tile, new_tile, idx_image)

    
class King(Piece):

    def __init__(self, tile, color, rook_left, rook_right):

        self.tile = tile
        self.color = color
        
        self.list_image = [white_king_image, black_king_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

        self.rook_left = rook_left
        self.rook_right = rook_right

    def update_possible_moves(self):
        
        board_pieces = self.get_board_pieces()
        self.available_moves = []

        # All moves of the king (four diagonal, two sense in horizontal direction and two sense in vertical direction => 8 possibility if no tile is out of range)
        for i in range(-1, 2):
            for j in range(-1, 2):
                # If the tile is not the same as the king
                if (i, j) != (0,0) and ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] + j <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = board_pieces[self.tile[0] + i][self.tile[1] + j]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
    
        self.castling_stroke()

    def tiles_empty(self, list_tile):

        for tile in list_tile:
            if self.get_board_pieces()[tile[0]][tile[1]] != None:
                return False
        return True

    def tiles_chess(self, list_tile):

        if self.color == 1:
            list_tile.append((7, 4))
            list_pieces = self.get_list_black_pieces()
        else:
            list_tile.append((0, 4))
            list_pieces = self.get_list_white_pieces()

        for piece in list_pieces:
            for tile in list_tile:
                if tile in piece.available_moves:
                    return True
        return False
    
    def castling_update(self, list_tiles_left, list_tiles_right, tiles_left_append, tiles_right_append):
         
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

        self.castling_update(DICO_TILES[self.color][0], DICO_TILES[self.color][1], DICO_TILES[self.color][2], DICO_TILES[self.color][3])
    
    def move_piece(self, current_tile, new_tile, idx_image):

        board_pieces = self.get_board_pieces()
    
        if self.first_move:
            # Right castling
            if new_tile == (7, 6) or new_tile == (0, 6):
                rook_piece = board_pieces[new_tile[0]][7]
                board_pieces[new_tile[0]][5] = rook_piece
                board_pieces[new_tile[0]][7] = None
                rook_piece.tile = (new_tile[0], 5)
                rook_piece.first_move = False
                super().move_piece(current_tile, new_tile, idx_image)
                return "castling"

            # Left castling
            elif new_tile == (7, 2) or new_tile == (0, 2):
                rook_piece = board_pieces[new_tile[0]][0]
                board_pieces[new_tile[0]][0] = None
                board_pieces[new_tile[0]][3] = rook_piece
                rook_piece.tile = (new_tile[0], 3)
                rook_piece.first_move = False
                super().move_piece(current_tile, new_tile, idx_image)
                return "castling"

        # Basic move
        return super().move_piece(current_tile, new_tile, idx_image)


class Knight(Piece):

    def __init__(self, tile, color):

        self.tile = tile
        self.color = color
        
        self.list_image = [white_knight_image, black_knight_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

    def update_possible_moves(self):
        
        board_pieces = self.get_board_pieces()
        self.available_moves = []

        # All moves of the knight (two tiles in a direction and one tile in the perpendicular direction => in every sense => 8 possibility if no tile is out of range)
        for i in range(-2, 3, 4): # -2 or 2
            for j in range(-1, 2, 2): # -1 or 1
                if ((0 <= self.tile[0] + i <= 7) and (0 <= self.tile[1] + j <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = board_pieces[self.tile[0] + i][self.tile[1] + j]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + i, self.tile[1] + j))

                if ((0 <= self.tile[0] + j <= 7) and (0 <= self.tile[1] + i <= 7)):
                    # If the tile is empty or is occupied by an opponent piece
                    piece = board_pieces[self.tile[0] + j][self.tile[1] + i]
                    if piece == None:
                        self.available_moves.append((self.tile[0] + j, self.tile[1] + i))
                    elif piece.color == -self.color:
                        self.available_moves.append((self.tile[0] + j, self.tile[1] + i))


class Rook(Piece):

    def __init__(self, tile, color):
        
        self.tile = tile
        self.color = color

        self.list_image = [white_rook_image, black_rook_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

    def update_possible_moves(self):
         
        board_pieces = self.get_board_pieces()
        self.available_moves = []

        # Vertical moves (Up)
        for i in range(1, self.tile[0] + 1):
            # If the tile is empty
            piece = board_pieces[self.tile[0] - i][self.tile[1]]
            if piece == None:
                self.available_moves.append((self.tile[0] - i, self.tile[1]))
            # If the tile is occupied by an opponent piece
            elif piece.color == -self.color:
                self.available_moves.append((self.tile[0] - i, self.tile[1]))
                break
            else:
                break
        
        # Vertical moves (Down)
        for i in  range(1, ROW - self.tile[0]):
            # If the tile is empty
            piece = board_pieces[self.tile[0] + i][self.tile[1]]
            if piece == None:
                self.available_moves.append((self.tile[0] + i, self.tile[1]))
            # If the tile is occupied by an opponent piece
            elif piece.color == - self.color:
                self.available_moves.append((self.tile[0] + i, self.tile[1]))  
                break
            else:
                break

        # Horizontal moves (Left)
        for i in range(1, self.tile[1] + 1):
            # If the tile is empty
            piece = board_pieces[self.tile[0]][self.tile[1] - i]
            if piece == None:
                self.available_moves.append((self.tile[0], self.tile[1] - i))
            # If the tile is occupied by an opponent piece
            elif piece.color == - self.color:
                self.available_moves.append((self.tile[0], self.tile[1] - i))   
                break
            else:
                break

        # Horizontal moves (Right)
        for i in range(1, COL - self.tile[1]):
            # If the tile is empty
            piece = board_pieces[self.tile[0]][self.tile[1] + i]
            if piece == None:
                self.available_moves.append((self.tile[0], self.tile[1] + i))
            # If the tile is occupied by an opponent piece
            elif piece.color == - self.color:
                self.available_moves.append((self.tile[0], self.tile[1] + i))  
                break 
            else:
                break 


class Bishop(Piece):

    def __init__(self, tile, color):
        
        self.tile = tile
        self.color = color
        
        self.list_image = [white_bishop_image, black_bishop_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

    def update_possible_moves(self):

        board_pieces = self.get_board_pieces()
        self.available_moves = []

        # Diagonal Left-Up
        for i in range(1, ROW):
            # If the tile is empty
            if ((0 <= self.tile[0] - i <= 7) and (0 <= self.tile[1] - i <= 7)):
                piece = board_pieces[self.tile[0] - i][self.tile[1] - i]
                if piece == None:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif board_pieces[self.tile[0] - i][self.tile[1] - i].color == - self.color:
                    self.available_moves.append((self.tile[0] - i, self.tile[1] - i))   
                    break
                else:
                    break

        # Diagonal Left-Down
        for i in range(1, ROW):
            if ((0 <= self.tile[0] - i <= 7) and (0 <= self.tile[1] + i <= 7)):
                # If the tile is empty
                piece = board_pieces[self.tile[0] - i][self.tile[1] + i]
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
                piece = board_pieces[self.tile[0] + i][self.tile[1] - i]
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
                piece = board_pieces[self.tile[0] + i][self.tile[1] + i]
                if piece == None:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif piece.color == - self.color:
                    self.available_moves.append((self.tile[0] + i, self.tile[1] + i))   
                    break
                else:
                    break


class Queen(Piece):

    def __init__(self, tile, color):
        
        self.tile = tile
        self.color = color
       
        self.list_image = [white_queen_image, black_queen_image]
        self.images = self.get_image(color, self.list_image)
        self.image = self.images[0]

        self.first_move = True
        self.just_moved = False
        self.available_moves = []

    def update_possible_moves(self):

        # Queen = Bishop + Rook
        bishop = Bishop(self.tile, self.color)
        rook = Rook(self.tile, self.color)

        bishop.update_possible_moves()
        rook.update_possible_moves()

        self.available_moves = (rook.available_moves + bishop.available_moves)

        bishop = None
        rook = None