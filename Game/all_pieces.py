import sys
sys.path.append("/Users/mathisdelsart/PycharmProjects/Chess-Game Project/Chess-Game/Game/All_Configs")
from Configs import ROW, COL

"""
These class represent the object of a single piece that have some characteristics and some methods.
=> The common characteristics are:
- The color of the piece (white : 1 or black : 1)
- The tile where the piece is on the board (the tile is a tuple (row, column))
- A variable for the first move of the piece (True or False) => True if the piece hasn't played yet, False otherwise

=> The main method are:
- update_possible_moves(): Update the list of possible basics moves of the piece (Doesn't take into account if the king
  is in Chess or not, if the move is legal,...
  => Other methods are called to reupdate the list of possible moves in the class Pieces)
"""

class Pawn:
    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move
        self.just_moved = False # Special variable for the special stroke "En Passant"

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        list_possible_moves = []
        # Normal move
        if dico_board[(self.tile[0] - self.color, self.tile[1])][2] == 0: # If the tile above the pawn is empty
            list_possible_moves.append((self.tile[0] - self.color, self.tile[1])) # Add the tile to the possible moves

            if self.first_move: # If the pawn is on its first move and the tile above is empty
                # Move 2 tiles (if first_move is True!)
                if dico_board[(self.tile[0] - 2 * self.color, self.tile[1])][2] == 0: # If the tile above (x2) the pawn is empty
                    list_possible_moves.append((self.tile[0] - 2 * self.color, self.tile[1])) # Add the tile to the possible moves

        # Diagonal moves if the pawn can eat an oponent piece
        for i in range(-1, 2, 2): # i = -1 or 1
            try:
                if dico_board[self.tile[0] - self.color, self.tile[1] + i][2] == - self.color: # If the tile diagonally above the pawn is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0] - self.color, self.tile[1] + i)) # Add the tile to the possible moves
            except:
                pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        return list_possible_moves

    def EnPassantMove(self):
        """
        Update a list with the possible "EnPassant" move (max 2 possibility).
        if there is no possible "EnPassant" move => boolean = False.
        Otherwise boolean = True => Will be add to the basic moves in the file Pieces.py.
        :return: boolean, list_possible_moves_enpassant
        """
        # Special Stroke ! ("En Passant")
        from Variables import dico_board
        list_possible_moves_enpassant = []
        right_tile = (self.tile[0], self.tile[1] + 1)
        try:
            if type(dico_board[right_tile][0]) == type(self) and dico_board[right_tile][0].just_moved: # If the tile to the right is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
                list_possible_moves_enpassant.append((self.tile[0] - self.color, self.tile[1] + 1)) # Add the tile to the possible moves
        except:
            pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        left_tile = (self.tile[0], self.tile[1] - 1)
        try:
            if type(dico_board[left_tile][0]) == type(self) and dico_board[left_tile][0].just_moved: # If the tile to the left is occupied by an opponent pawn and the pawn just moved of two tiles (his first move)
                list_possible_moves_enpassant.append((self.tile[0] - self.color, self.tile[1] - 1)) # Add the tile to the possible moves
        except:
            pass # Deal with the out of range error (By example, if the pawn is on the last column and the player want to move it to the diagonal RIGHT, the program will raise an error)

        if list_possible_moves_enpassant == []:
            return False, None
        else:
            return True, list_possible_moves_enpassant

class King:
    def __init__(self, tile, color, first_move, rook_1, rook_2):
        self.tile = tile
        self.color = color
        self.first_move = first_move
        self.rook_1 = rook_1 # Rook left of the king
        self.rook_2 = rook_2 # Rook right of the king

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        list_possible_moves = []
        # All moves of the king (four diagonal, two sense in horizontal direction and two sense in vertical direction => 8 possibility if no tile is out of range)
        for i in range(-1, 2): # i = -1 / 1 or 0
            for j in range(-1, 2): # j = -1 / 1 or 0
                try:
                    if (i, j) != (0,0): # If the tile is not the same as the king (he can move on the same tile :))
                        if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]: # If the tile is empty or is occupied by an opponent piece
                            list_possible_moves.append((self.tile[0] + i, self.tile[1] + j)) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error

        return list_possible_moves

    def Rook_LeftStroke(self):
        """
        boolean = True if the king and the left rook are on their first move.
        Otherwise, boolean = False
        :return: boolean
        """
        if self.first_move and self.rook_1.first_move: # If the king is on its first move and the rook left is on its first move
            return True
        return False

    def Rook_RightStroke(self):
        """
        boolean = True if the king and the right rook are on their first move.
        Otherwise, boolean = False
        :return: boolean
        """
        if self.first_move and self.rook_2.first_move: # If the king is on its first move and the rook right is on its first move
            return True
        return False

class Knight:
    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        list_possible_moves = []
        for i in range(-2, 3, 4): # i = -2 or 2
            for j in range(-1, 2, 2): # j = -1 or 1
                # All moves of the knight (TWO tiles in a direction and ONE tile in the PERPENDICULAR direction => in every sense => 8 possibility if no tile is out of range)
                try:
                    if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]: # If the tile is empty or is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] + j)) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error$
                try:
                    if dico_board[(self.tile[0] + j, self.tile[1] + i)][2] in [0, - self.color]: # If the tile is empty or is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] + j, self.tile[1] + i)) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error

        return list_possible_moves

class Rook:
    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        list_possible_moves = []
        # Vertical moves (Up)
        try:
            for i in range(1, self.tile[0] + 1):
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == 0: # If the tile is empty
                    list_possible_moves.append((self.tile[0] - i, self.tile[1])) # Add the tile to the possible moves
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == - self.color: # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0] - i, self.tile[1])) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0] - i, self.tile[1])][2] == self.color: # If the tile is occupied by an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error
        # Vertical moves (Down)
        try:
            for i in  range(1, ROW - self.tile[0] + 1):
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == 0: # If the tile is empty
                    list_possible_moves.append((self.tile[0] + i, self.tile[1])) # Add the tile to the possible moves
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == - self.color: # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0] + i, self.tile[1])) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0] + i, self.tile[1])][2] == self.color: # If the tile is occupied by an ally piece
                    break # Stop the loop
        except:
            pass
        # Horizontal moves (Left)
        try:
            for i in range(1, self.tile[1] + 1):
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == 0: # If the tile is empty
                    list_possible_moves.append((self.tile[0], self.tile[1] - i)) # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == - self.color: # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))  # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] - i)][2] == self.color: # If the tile is occupied by an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error
        # Horizontal moves (Right)
        try:
            for i in range(1, COL - self.tile[1] + 1):
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == 0: # If the tile is empty
                    list_possible_moves.append((self.tile[0], self.tile[1] + i)) # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == - self.color: # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0], self.tile[1] + i)) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] + i)][2] == self.color: # If the tile is occupied by an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error

        return list_possible_moves

class Bishop:
    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        list_possible_moves = []
        # All the necessary enters to make the bishop move (the four diagonals)
        enter_left_down = True
        enter_left_up = True
        enter_right_up = True
        enter_right_down = True

        for i in range(1, ROW):
            # Diagonal Left-Up
            try:
                if enter_left_up:
                    if dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append((self.tile[0] - i, self.tile[1] - i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] - i, self.tile[1] - i))  # Add the tile to the possible moves
                        enter_left_up = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == self.color:  # If the tile is occupied by an ally piece
                        enter_left_up = False
            except:
                enter_left_up = False  # Deal with the out of range error (The bishop can't go further left up)
            # Diagonal Left-Down
            try:
                if enter_left_down:
                    if dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append((self.tile[0] - i, self.tile[1] + i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] - i, self.tile[1] + i))  # Add the tile to the possible moves
                        enter_left_down = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == self.color:  # If the tile is occupied by an ally piece
                        enter_left_down = False
            except:
                enter_left_down = False  # Deal with the out of range error (The bishop can't go further left down)
            # Diagonal Right-Up
            try:
                if enter_right_up:
                    if dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] - i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == - self.color: # If the tile is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] - i))  # Add the tile to the possible moves
                        enter_right_up = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == self.color:  # If the tile is occupied by an ally piece
                        enter_right_up = False
            except:
                enter_right_up = False  # Deal with the out of range error (The bishop can't go further right up)
            # Diagonal Right-Down
            try:
                if enter_right_down:
                    if dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == - self.color: # If the tile is occupied by an opponent piece
                        list_possible_moves.append((self.tile[0] + i, self.tile[1] + i))  # Add the tile to the possible moves
                        enter_right_down = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == self.color:  # If the tile is occupied by an ally piece
                        enter_right_down = False
            except:
                enter_right_down = False  # Deal with the out of range error (The bishop can't go further right down)

        return list_possible_moves

class Queen:
    def __init__(self, tile, color, first_move):
        self.tile = tile
        self.color = color
        self.first_move = first_move
        self.promoted = False  # Special variable for the promotion

    def update_possible_moves(self):
        """
        Update the basic possible moves (without check,...)
        :return: list_possible_moves = list of all the basic possibles moves
                 Example : list_possible_moves = [(5,3), (5,4), (7,3)]
        """
        from Variables import dico_board
        # Bishop move
        list_possible_moves = []
        # All the necessary enters to make the bishop move (the four diagonals)
        enter_left_down = True
        enter_left_up = True
        enter_right_up = True
        enter_right_down = True

        for i in range(1, ROW):
            # Diagonal Left-Up
            try:
                if enter_left_up:
                    if dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append(
                            (self.tile[0] - i, self.tile[1] - i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][
                        2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append(
                            (self.tile[0] - i, self.tile[1] - i))  # Add the tile to the possible moves
                        enter_left_up = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][
                        2] == self.color:  # If the tile is occupied by an ally piece
                        enter_left_up = False
            except:
                enter_left_up = False  # Deal with the out of range error (The bishop can't go further left up)
            # Diagonal Left-Down
            try:
                if enter_left_down:
                    if dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append(
                            (self.tile[0] - i, self.tile[1] + i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][
                        2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append(
                            (self.tile[0] - i, self.tile[1] + i))  # Add the tile to the possible moves
                        enter_left_down = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][
                        2] == self.color:  # If the tile is occupied by an ally piece
                        enter_left_down = False
            except:
                enter_left_down = False  # Deal with the out of range error (The bishop can't go further left down)
            # Diagonal Right-Up
            try:
                if enter_right_up:
                    if dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append(
                            (self.tile[0] + i, self.tile[1] - i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][
                        2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append(
                            (self.tile[0] + i, self.tile[1] - i))  # Add the tile to the possible moves
                        enter_right_up = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][
                        2] == self.color:  # If the tile is occupied by an ally piece
                        enter_right_up = False
            except:
                enter_right_up = False  # Deal with the out of range error (The bishop can't go further right up)
            # Diagonal Right-Down
            try:
                if enter_right_down:
                    if dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == 0:  # If the tile is empty
                        list_possible_moves.append(
                            (self.tile[0] + i, self.tile[1] + i))  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][
                        2] == - self.color:  # If the tile is occupied by an opponent piece
                        list_possible_moves.append(
                            (self.tile[0] + i, self.tile[1] + i))  # Add the tile to the possible moves
                        enter_right_down = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][
                        2] == self.color:  # If the tile is occupied by an ally piece
                        enter_right_down = False
            except:
                enter_right_down = False  # Deal with the out of range error (The bishop can't go further right down)

        # Rook move

        # Vertical moves (Up)
        try:
            for i in range(1, self.tile[0] + 1):
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == 0:  # If the tile is empty
                    list_possible_moves.append(
                        (self.tile[0] - i, self.tile[1]))  # Add the tile to the possible moves
                if dico_board[(self.tile[0] - i, self.tile[1])][ 2] == - self.color:  # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0] - i, self.tile[1]))  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0] - i, self.tile[1])][2] == self.color:  # If the tile is occupied by an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error
        # Vertical moves (Down)
        try:
            for i in range(1, ROW - self.tile[0] + 1):
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == 0:  # If the tile is empty
                    list_possible_moves.append((self.tile[0] + i, self.tile[1]))  # Add the tile to the possible moves
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == - self.color:  # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0] + i, self.tile[1]))  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0] + i, self.tile[1])][2] == self.color:  # If the tile is occupied by an ally piece
                    break  # Stop the loop
        except:
            pass
        # Horizontal moves (Left)
        try:
            for i in range(1, self.tile[1] + 1):
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == 0:  # If the tile is empty
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))  # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == - self.color:  # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0], self.tile[1] - i))  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] - i)][2] == self.color:  # If the tile is occupied by an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error
        # Horizontal moves (Right)
        try:
            for i in range(1, COL - self.tile[1] + 1):
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == 0:  # If the tile is empty
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))  # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == - self.color:  # If the tile is occupied by an opponent piece
                    list_possible_moves.append((self.tile[0], self.tile[1] + i))  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] + i)][2] == self.color:  # If the tile is occupied by an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error

        return list_possible_moves