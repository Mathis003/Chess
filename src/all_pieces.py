from src.assets import *


"""
These classes represent the object of a single piece that have some characteristics and some methods.
=> The common characteristics are:
- The color of the piece (white : 1 or black : -1)
- The tile where the piece is on the board (the tile is a tuple (row, column))
- A variable for the first move of the piece (True or False) => True if the piece hasn't played yet, False otherwise

=> The main method are:
- update_possible_moves(): Update the list of possible basics moves of the piece (Doesn't take into account if the king
  is in Chess or not, if the move is legal (don't put the king in Chess),...
  => Other methods are called to reupdate the list of possible moves in the class Pieces).
"""


"""
Parent class
"""
class Piece:

    def __init__(self, board, tile, color, available_moves, list_images, current_idx_image, first_move):
        self.board = board
        self.tile = tile
        self.color = color
        self.available_moves = available_moves
        self.list_images = list_images
        self.current_idx_image = current_idx_image
        self.image = self.list_images[self.current_idx_image]
        self.first_move = first_move
    
    def get_mod_move(self, new_tile):
        """
        If the move is 'check' or 'stalemate, the variable will be updated again later.
        """
        if self.board[new_tile[0]][new_tile[1]].color != 0:
            return "capture"
        else:
            return "move"
    
    def update_possible_moves(self):
        return ""

    def add_piece(self, piece):
        if piece.color == 1:
            self.board.LIST_WHITE_PIECES.append(piece)
        elif piece.color == -1:
            self.board.LIST_BLACK_PIECES.append(piece)

    def remove_piece(self, piece):
        if piece != None:
            if piece.color == 1:
                self.board.LIST_WHITE_PIECES.remove(piece)
            elif piece.color == -1:
                self.board.LIST_BLACK_PIECES.remove(piece)
    
    def move_piece(self, current_tile, new_tile):

        mod_of_move = self.get_mod_move(new_tile)
        piece = self.board[new_tile[0]][new_tile[1]]
        self.remove_piece(piece)

        self.board[new_tile[0]][new_tile[1]] = self
        self.board[current_tile[0]][current_tile[1]] = None

        self.tile = new_tile

        if self.first_move:
            self.first_move = False

        return mod_of_move

class Pawn(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)
        self.just_moved = False # Variable for the special stroke "En Passant"

    def update_possible_moves(self):
         
        list_possible_moves = []

        # If the tile above the pawn is empty
        if self.board[self.tile[0] - self.color][self.tile[1]].color == 0:
            list_possible_moves.append((self.tile[0] - self.color, self.tile[1]))
            
            # If the pawn is on its first move and the tile above is empty
            if self.first_move:
                # If the tile above (x2) the pawn is empty (special stroke when first move)
                if self.board[self.tile[0] - 2 * self.color][self.tile[1]].color == 0:
                    list_possible_moves.append((self.tile[0] - 2 * self.color, self.tile[1]))

        # Attack moves
        for i in range(-1, 2, 2):
            try:
                # If the tile diagonally above the pawn is occupied by an opponent piece
                if self.board[self.tile[0] - self.color][self.tile[1] + i].color == - self.color:
                    list_possible_moves.append((self.tile[0] - self.color, self.tile[1] + i))
            except:
                pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        return list_possible_moves

    def move_en_passant(self):
        """
        Return a list with the possible "En Passant" move (max 2 possibility).
        """
         
        list_possible_moves_enpassant = []

        try:
            right_tile = (self.tile[0], self.tile[1] + 1)
            piece_right = self.board[right_tile[0]][right_tile[1]]
            # If the tile to the right is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if type(piece_right) == type(self) and piece_right.just_moved:
                list_possible_moves_enpassant.append((self.tile[0] - self.color, self.tile[1] + 1))
        except:
            pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        try:
            left_tile = (self.tile[0], self.tile[1] - 1)
            piece_left = self.board[left_tile[0]][left_tile[1]]
            # If the tile to the left is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if type(piece_left) == type(self) and piece_left.just_moved:
                list_possible_moves_enpassant.append((self.tile[0] - self.color, self.tile[1] - 1))
        except:
            pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        return list_possible_moves_enpassant

    def move_piece(self, current_tile, new_tile, idx_image):

        # If the pawn can be promoted.
        if new_tile[0] == 0 or new_tile[0] == 7:

            mod_of_move = self.get_mod_move(new_tile)
            if self.color == 1:
                image_queen = white_queen_image[idx_image]
            else:
                image_queen = black_queen_image[idx_image]

            new_queen = Queen(new_tile, self.color, image_queen, False)
            self.remove_piece(new_tile)
            self.remove_piece(current_tile)
            self.add_piece(new_queen)
            new_queen.promoted = True

            self.board[new_tile[0]][new_tile[1]] = new_queen
            self.board[current_tile[0]][current_tile[1]] = None

        else:
            # If the piece is a pawn that move to an empty tile.
            if self.board[new_tile[0]][new_tile[1]] == None:
                # If the pawn can do the move 'en passant'.
                if new_tile == (current_tile[0] - self.color, current_tile[1] + 1) or new_tile == (current_tile[0] - self.color, current_tile[1] - 1):

                    tile_piece_eaten = (current_tile[0], new_tile[1])
                    piece_eaten = self.board[tile_piece_eaten[0]][tile_piece_eaten[1]]
                    self.board.dico_list_pieces[-self.color].remove(piece_eaten)
                    mod_of_move =  "capture"
                else:
                    mod_of_move = "move"
                
                self.board[new_tile[0]][new_tile[1]] = self
                self.board[current_tile[0]][current_tile[1]] = None

                if self.first_move:
                    # If the pawn has moved 2 tiles.
                    if abs(current_tile[0] - new_tile[0]) == 2:
                        self.just_moved = True
                else:
                    self.just_moved = False
            else:
                # If the pawn move to atack a piece (basic move).
                mod_of_move =  "capture"
                self.remove_piece(new_tile)
                self.board[new_tile[0]][new_tile[1]] = self
                self.board[current_tile[0]][current_tile[1]] = None

        self.tile = new_tile

        if self.first_move:
            self.first_move = False  

        return mod_of_move

class King(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move, rook_left, rook_right):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)
        self.rook_left = rook_left # Rook at the left of the king
        self.rook_right = rook_right # Rook at the right of the king

    def update_possible_moves(self):
         
        list_possible_moves = []

        # All moves of the king (four diagonal, two sense in horizontal direction and two sense in vertical direction => 8 possibility if no tile is out of range)
        for i in range(-1, 2):
            for j in range(-1, 2):
                # If the tile is not the same as the king
                if (i, j) != (0,0):
                    try:
                        # If the tile is empty or is occupied by an opponent piece
                        if self.board[self.tile[0] + i][self.tile[1] + j].color in [0, -self.color]:
                            list_possible_moves.append((self.tile[0] + i, self.tile[1] + j))
                    except:
                        pass # Deal with the out of range error
                
        return list_possible_moves

    def tiles_empty(self, list_tile):

        for tile in list_tile:
            if self.board[tile[0]][tile[1]].color != 0:
                return False
        return True

    def tiles_chess(self, list_tile):

        if self.color == 1:
            list_tile.append((7, 4))
        else:
            list_tile.append((0, 4))

        for piece in self.board.dico_list_pieces[-self.color]:
            list_possible_moves = piece.update_possible_moves()
            for tile in list_tile:
                if tile in list_possible_moves:
                    return True
        return False
    
    def castling_aux(self, list_tiles_left, list_tiles_right, tiles_left_append, tiles_right_append):
         
        if self.first_move:
            if self.rook_left.first_move:
                # If the tiles between the king and the left rook are empty and not in check
                if self.tiles_empty(list_tiles_left) and not self.tiles_chess(list_tiles_left):
                    self.board[self.tile[0]][self.tile[1]].available_moves.append(tiles_left_append)

            # If the king and the right rook haven't played yet
            if self.rook_right.first_move:
                # If the tiles between the king and the right rook are empty and not in check
                if self.tiles_empty(list_tiles_right) and not self.tiles_chess(list_tiles_right):
                    self.board[self.tile[0]][self.tile[1]].available_moves.append(tiles_right_append)

    def castling_stroke(self):

        # color : [list_tile_left_stroke, list_tile_right_stroke, tile_to_append_left, tile_to_append_right]
        DICO_TILES = {1 : [[(7, 5), (7, 6)], [(7, 3), (7, 2), (7, 1)], (7, 6), (7, 2)],
                     -1 : [[(0, 5), (0, 6)], [(0, 3), (0, 2), (0, 1)], (0, 6), (0, 2)]}

        self.castling_aux(DICO_TILES[self.color][0], DICO_TILES[self.color][1], DICO_TILES[self.color][2], DICO_TILES[self.color][3])
    
    def move_piece(self, current_tile, new_tile, idx_image):

        if self.first_move:
            # Right castling
            if new_tile == (7, 6) or new_tile == (0, 6):

                self.board[new_tile[0]][6] = self.board[new_tile[0]][4]
                self.board[new_tile[0]][7] = None
                rook_piece = self.board[new_tile[0]][5]
                rook_piece.tile = (new_tile[0], 5)
                rook_piece.first_move = False
                self.first_move = False
                self.tile = new_tile
                return "castling"

            # Left castling
            elif new_tile == (7, 2) or new_tile == (0, 2):
                self.board[new_tile[0]][2] = self.board[new_tile[0]][4]
                self.board[new_tile[0]][0] = None
                rook_piece = self.board[new_tile[0]][3]
                rook_piece.tile = (new_tile[0], 3)
                rook_piece.first_move = False
                self.first_move = False
                self.tile = new_tile
                return "castling"
            else:
                self.first_move = False

        # Basic move
        mod_of_move = self.get_mod_move(new_tile)
        self.remove_piece(new_tile)   
        self.board[new_tile[0]][new_tile[1]] = self
        self.board[current_tile[0]][current_tile[1]] = None
        self.tile = new_tile
        return mod_of_move


class Knight(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):
         
        list_possible_moves = []

        # All moves of the knight (two tiles in a direction and one tile in the perpendicular direction => in every sense => 8 possibility if no tile is out of range)
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                try:
                    # If the tile is empty or is occupied by an opponent piece
                    if self.board[self.tile[0] + i][self.tile[1]+ j].color in [0, - self.color]:
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] + j))
                except:
                    pass # Deal with the out of range error$
                try:
                    # If the tile is empty or is occupied by an opponent piece
                    if self.board[self.tile[0] + j][self.tile[1]+ i].color in [0, - self.color]:
                        list_possible_moves.append((self.tile[0] + j, self.tile[1] + i))
                except:
                    pass # Deal with the out of range error

        return list_possible_moves


class Rook(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):
         
        list_possible_moves = []

        # Vertical moves (Up)
        try:
            for i in range(1, self.tile[0] + 1):
                # If the tile is empty
                if self.board[self.tile[0] - i][self.tile[1]].color == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] - i][self.tile[1]].color == -self.color:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1]))
                    break
                else:
                    break
        except:
            pass # Deal with the out of range error
        
        # Vertical moves (Down)
        try:
            for i in  range(1, ROW - self.tile[0] + 1):
                # If the tile is empty
                if self.board[self.tile[0] + i][self.tile[1]].color == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] + i][self.tile[1]].color == - self.color:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1]))  
                    break
                else:
                    break
        except:
            pass

        # Horizontal moves (Left)
        try:
            for i in range(1, self.tile[1] + 1):
                # If the tile is empty
                if self.board[self.tile[0]][self.tile[1] - i].color == 0:
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0]][self.tile[1] - i].color == - self.color:
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))   
                    break
                else:
                    break
        except:
            pass # Deal with the out of range error

        # Horizontal moves (Right)
        try:
            for i in range(1, COL - self.tile[1] + 1):
                # If the tile is empty
                if self.board[self.tile[0]][self.tile[1] + i].color == 0:
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0]][self.tile[1] + i].color == - self.color:
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))  
                    break 
                else:
                    break 
        except:
            pass # Deal with the out of range error

        return list_possible_moves


class Bishop(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)

    def update_possible_moves(self):

        list_possible_moves = []

        # Diagonal Left-Up
        for i in range(1, ROW):
            try:
                # If the tile is empty
                if self.board[self.tile[0] - i][self.tile[1] - i].color == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] - i][self.tile[1] - i].color == - self.color:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] - i))   
                    break
                else:
                    break
            except:
                pass # Deal with the out of range error (The bishop can't go further left up)

        # Diagonal Left-Down
        for i in range(1, ROW):
            try:
                # If the tile is empty
                if self.board[self.tile[0] - i][self.tile[1] + i].color == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] - i][self.tile[1] + i].color == - self.color:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] + i))   
                    break
                else:
                    break
            except:
                pass # Deal with the out of range error (The bishop can't go further left down)

        # Diagonal Right-Up
        for i in range(1, ROW):
            try:
                # If the tile is empty
                if self.board[self.tile[0] + i][self.tile[1] - i].color == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] + i][self.tile[1] - i].color == - self.color:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] - i))   
                    break
                else:
                    break
            except:
                pass # Deal with the out of range error (The bishop can't go further right up)

        # Diagonal Right-Down
        for i in range(1, ROW):
            try:
                # If the tile is empty
                if self.board[self.tile[0] + i][self.tile[1] + i].color == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif self.board[self.tile[0] + i][self.tile[1] + i].color == - self.color:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))   
                    break
                else:
                    break
            except:
                pass # Deal with the out of range error (The bishop can't go further right down)

        return list_possible_moves


class Queen(Piece):

    def __init__(self, tile, color, available_moves, list_images, current_idx_image, first_move):
        super().__init__(None, tile, color, available_moves, list_images, current_idx_image, first_move)
        self.promoted = False  # Special variable for the promotion

    def update_possible_moves(self):

        bishop = Bishop(self.tile, self.color, self.first_move)
        list_possible_moves_bishop = bishop.update_possible_moves()
        bishop = None

        rook = Rook(self.tile, self.color, self.first_move)
        list_possible_moves_rook = rook.update_possible_moves()
        rook = None

        return (list_possible_moves_rook + list_possible_moves_bishop)