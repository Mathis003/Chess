from src.all_configs.assets import *


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

    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move
    
    def get_mod_move(self, new_tile):
        """
        If the move is 'check' or 'stalemate, the variable will be updated again later.
        """
        if dico_board[new_tile][2] != 0:
            return "capture"
        else:
            return "move"
    
    def update_possible_moves(self):
        return ""

    def add_piece(self, piece):
        if piece.color == 1:
            LIST_WHITE_PIECES.append(piece)
        elif piece.color == -1:
            LIST_BLACK_PIECES.append(piece)

    def remove_piece(self, tile):

        if dico_board[tile][0] != None:
            if dico_board[tile][2] == 1:
                LIST_WHITE_PIECES.remove(dico_board[tile][0])
            elif dico_board[tile][2] == -1:
                LIST_BLACK_PIECES.remove(dico_board[tile][0])
    
    def move_piece(self, current_tile, new_tile, idx_image):

        mod_of_move = self.get_mod_move(new_tile)
        self.remove_piece(new_tile)   
        dico_board[new_tile] = [self, dico_board[current_tile][1], dico_board[current_tile][2], []]
        dico_board[current_tile] = [None, None, 0, []]

        self.tile = new_tile

        if self.first_move:
            self.first_move = False

        return mod_of_move

class Pawn(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)
        self.just_moved = False # Variable for the special stroke "En Passant"

    def update_possible_moves(self):
         
        list_possible_moves = []

        # If the tile above the pawn is empty
        if dico_board[(self.tile[0] - self.color, self.tile[1])][2] == 0:
            list_possible_moves.append((self.tile[0] - self.color, self.tile[1]))
            
            # If the pawn is on its first move and the tile above is empty
            if self.first_move:
                # If the tile above (x2) the pawn is empty (special stroke when first move)
                if dico_board[(self.tile[0] - 2 * self.color, self.tile[1])][2] == 0:
                    list_possible_moves.append((self.tile[0] - 2 * self.color, self.tile[1]))

        # Attack moves
        for i in range(-1, 2, 2):
            try:
                # If the tile diagonally above the pawn is occupied by an opponent piece
                if dico_board[self.tile[0] - self.color, self.tile[1] + i][2] == - self.color:
                    list_possible_moves.append((self.tile[0] - self.color, self.tile[1] + i))
            except:
                pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        return list_possible_moves

    def move_en_passant(self):
        """
        Return a list with the possible "En Passant" move (max 2 possibility).
        """
         
        list_possible_moves_enpassant = []

        right_tile = (self.tile[0], self.tile[1] + 1)
        try:
            # If the tile to the right is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if type(dico_board[right_tile][0]) == type(self) and dico_board[right_tile][0].just_moved:
                list_possible_moves_enpassant.append((self.tile[0] - self.color, self.tile[1] + 1))
        except:
            pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        left_tile = (self.tile[0], self.tile[1] - 1)
        try:
            # If the tile to the left is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
            if type(dico_board[left_tile][0]) == type(self) and dico_board[left_tile][0].just_moved:
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

            new_queen = Queen(new_tile, self.color, False)
            self.remove_piece(new_tile)
            self.remove_piece(current_tile)
            self.add_piece(new_queen)
            dico_board[current_tile] = [None, None, 0, []]
            dico_board[new_tile] = [new_queen, image_queen, new_queen.color, []]
            new_queen.promoted = True

        else:
            # If the piece is a pawn that move to an empty tile.
            if dico_board[new_tile][2] == 0:
                # If the pawn can do the move 'en passant'.
                if new_tile == (current_tile[0] - self.color, current_tile[1] + 1) or new_tile == (current_tile[0] - self.color, current_tile[1] - 1):

                    tile_piece_eaten = (current_tile[0], new_tile[1])
                    piece_eaten = dico_board[tile_piece_eaten][0]
                    dico_list_pieces[- self.color].remove(piece_eaten)
                    dico_board[tile_piece_eaten] = [None, None, 0, []]
                    mod_of_move =  "capture"
                else:
                    mod_of_move = "move"

                dico_board[new_tile] = [self, dico_board[current_tile][1], dico_board[current_tile][2], []]
                dico_board[current_tile] = [None, None, 0, []]

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
                dico_board[new_tile] = [self, dico_board[current_tile][1], dico_board[current_tile][2], []]
                dico_board[current_tile] = [None, None, 0, []]

        self.tile = new_tile

        if self.first_move:
            self.first_move = False  

        return mod_of_move

class King(Piece):

    def __init__(self, tile, color, first_move, rook_left, rook_right):
        super().__init__(tile, color, first_move)
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
                        if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]:
                            list_possible_moves.append((self.tile[0] + i, self.tile[1] + j))
                    except:
                        pass # Deal with the out of range error
                
        return list_possible_moves

    def tiles_empty(self, list_tile):

        for tile in list_tile:
            if dico_board[tile][2] != 0:
                return False
        return True

    def tiles_chess(self, list_tile):

        if self.color == 1:
            list_tile.append((7, 4))
        else:
            list_tile.append((0, 4))

        for piece in dico_list_pieces[-self.color]:
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
                    dico_board[self.tile][3].append(tiles_left_append)

            # If the king and the right rook haven't played yet
            if self.rook_right.first_move:
                # If the tiles between the king and the right rook are empty and not in check
                if self.tiles_empty(list_tiles_right) and not self.tiles_chess(list_tiles_right):
                    dico_board[self.tile][3].append(tiles_right_append)

    def castling_stroke(self):

        # color : [list_tile_left_stroke, list_tile_right_stroke, tile_to_append_left, tile_to_append_right]
        DICO_TILES = {1 : [[(7, 5), (7, 6)], [(7, 3), (7, 2), (7, 1)], (7, 6), (7, 2)],
                     -1 : [[(0, 5), (0, 6)], [(0, 3), (0, 2), (0, 1)], (0, 6), (0, 2)]}

        self.castling_aux(DICO_TILES[self.color][0], DICO_TILES[self.color][1], DICO_TILES[self.color][2], DICO_TILES[self.color][3])
    
    def move_piece(self, current_tile, new_tile, idx_image):

        if self.first_move:
            # Right castling
            if new_tile == (7, 6) or new_tile == (0, 6):
                dico_board[(new_tile[0], 6)] = [dico_board[(new_tile[0], 4)][0], dico_board[(new_tile[0], 4)][1], dico_board[(new_tile[0], 4)][2], []]
                dico_board[(new_tile[0], 4)] = [None, None, 0, []]
                dico_board[(new_tile[0], 5)] = [dico_board[(new_tile[0], 7)][0], dico_board[(new_tile[0], 7)][1], dico_board[(new_tile[0], 7)][2], []]
                dico_board[(new_tile[0], 7)] = [None, None, 0, []]
                rook_piece = dico_board[(new_tile[0], 5)][0]
                rook_piece.tile = (new_tile[0], 5)
                rook_piece.first_move = False
                self.first_move = False
                self.tile = new_tile
                return "castling"

            # Left castling
            elif new_tile == (7, 2) or new_tile == (0, 2):
                dico_board[(new_tile[0], 2)] = [dico_board[(new_tile[0], 4)][0], dico_board[(new_tile[0], 4)][1], dico_board[(new_tile[0], 4)][2], []]
                dico_board[(new_tile[0], 4)] = [None, None, 0, []]
                dico_board[(new_tile[0], 3)] = [dico_board[(new_tile[0], 0)][0], dico_board[(new_tile[0], 0)][1], dico_board[(new_tile[0], 0)][2], []]
                dico_board[(new_tile[0], 0)] = [None, None, 0, []]
                rook_piece = dico_board[(new_tile[0], 3)][0]
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
        dico_board[new_tile] = [self, dico_board[current_tile][1], dico_board[current_tile][2], []]
        dico_board[current_tile] = [None, None, 0, []]
        
        self.tile = new_tile
        return mod_of_move


class Knight(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)

    def update_possible_moves(self):

         
        list_possible_moves = []

        # All moves of the knight (two tiles in a direction and one tile in the perpendicular direction => in every sense => 8 possibility if no tile is out of range)
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                try:
                    # If the tile is empty or is occupied by an opponent piece
                    if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]:
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] + j))
                except:
                    pass # Deal with the out of range error$
                try:
                    # If the tile is empty or is occupied by an opponent piece
                    if dico_board[(self.tile[0] + j, self.tile[1] + i)][2] in [0, - self.color]:
                        list_possible_moves.append((self.tile[0] + j, self.tile[1] + i))
                except:
                    pass # Deal with the out of range error

        return list_possible_moves


class Rook(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)

    def update_possible_moves(self):

         
        list_possible_moves = []

        # Vertical moves (Up)
        try:
            for i in range(1, self.tile[0] + 1):
                # If the tile is empty
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] - i, self.tile[1])][2] == - self.color:
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
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1]))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] + i, self.tile[1])][2] == - self.color:
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
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == 0:
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0], self.tile[1] - i)][2] == - self.color:
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
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == 0:
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0], self.tile[1] + i)][2] == - self.color:
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))  
                    break 
                else:
                    break 
        except:
            pass # Deal with the out of range error

        return list_possible_moves


class Bishop(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)

    def update_possible_moves(self):

        list_possible_moves = []

        # Diagonal Left-Up
        for i in range(1, ROW):
            try:
                # If the tile is empty
                if dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == - self.color:
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
                if dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == 0:
                    list_possible_moves.append((self.tile[0] - i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == - self.color:
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
                if dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] - i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == - self.color:
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
                if dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == 0:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))
                # If the tile is occupied by an opponent piece
                elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == - self.color:
                    list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))   
                    break
                else:
                    break
            except:
                pass # Deal with the out of range error (The bishop can't go further right down)

        return list_possible_moves


class Queen(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)
        self.promoted = False  # Special variable for the promotion

    def update_possible_moves(self):

        bishop = Bishop(self.tile, self.color, self.first_move)
        list_possible_moves_bishop = bishop.update_possible_moves()
        bishop = None

        rook = Rook(self.tile, self.color, self.first_move)
        list_possible_moves_rook = rook.update_possible_moves()
        rook = None

        return (list_possible_moves_rook + list_possible_moves_bishop)
    


"""
###
### Variables usefull in all the program! ###
###
"""


"""
Initialize all the pieces instances
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