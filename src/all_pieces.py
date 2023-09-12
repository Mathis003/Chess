from src.all_configs.configs import ROW, COL

"""
These classes represent the object of a single piece that have some characteristics and some methods.
=> The common characteristics are:
- The color of the piece (white : 1 or black : -1)
- The tile where the piece is on the board (the tile is a tuple (row, column))
- A variable for the first move of the piece (True or False) => True if the piece hasn't played yet, False otherwise

=> The main method are:
- update_possible_moves(): Update the list of possible basics moves of the piece (Doesn't take into account if the king
  is in Chess or not, if the move is legal,...
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
    
    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        return: list of all the basic possibles moves
                Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from src.all_configs.variables import dico_board
        return dico_board


class Pawn(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)
        self.just_moved = False # Variable for the special stroke "En Passant"

    def update_possible_moves(self):
        
        dico_board = super().update_possible_moves()
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

    def EnPassantMove(self):
        """
        Return a list with the possible "EnPassant" move (max 2 possibility).
        """
        dico_board = super().update_possible_moves()
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


class King(Piece):

    def __init__(self, tile, color, first_move, rook_left, rook_right):
        super().__init__(tile, color, first_move)
        self.rook_left = rook_left # Rook at the left of the king
        self.rook_right = rook_right # Rook at the right of the king

    def update_possible_moves(self):

        dico_board = super().update_possible_moves()
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

    def Rook_LeftStroke(self):
        """
        Return True if the king and the left rook are on their first move.
        Otherwise, return False.
        """
        return (self.first_move and self.rook_left.first_move)

    def Rook_RightStroke(self):
        """
        boolean = True if the king and the right rook are on their first move.
        Otherwise, boolean = False
        :return: boolean
        """
        return (self.first_move and self.rook_right.first_move)


class Knight(Piece):

    def __init__(self, tile, color, first_move):
        super().__init__(tile, color, first_move)

    def update_possible_moves(self):

        dico_board = super().update_possible_moves()
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

        dico_board = super().update_possible_moves()
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

        dico_board = super().update_possible_moves()
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