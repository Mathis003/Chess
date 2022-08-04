from Configs import *

class Pawn:
    def __init__(self, rect, tile, color, first_move):
        self.rect = rect # Rect of the piece's image
        self.tile = tile # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black
        self.first_move = first_move # Special variable for Pawn pieces

    def update_possible_moves(self):
        """ Update the possible moves of the pawn """
        from Assets import dico_board
        list_possible_moves = []
        if dico_board[(self.tile[0] - self.color, self.tile[1])][2] == 0: # If the tile above the pawn is empty
            list_possible_moves.append([self.tile[0] - self.color, self.tile[1]]) # Add the tile to the possible moves

            if self.first_move: # If the pawn is on its first move and the tile above is empty
                if dico_board[(self.tile[0] - 2 * self.color, self.tile[1])][2] == 0: # If the tile above (x2) the pawn is empty
                    list_possible_moves.append([self.tile[0] - 2 * self.color, self.tile[1]]) # Add the tile to the possible moves

        for i in range(-1, 2, 2): # i = -1 or 1
            try:
                if dico_board[self.tile[0] - self.color, self.tile[1] + i][2] == - self.color: # If the tile diagonally above the pawn is an opponent piece
                    list_possible_moves.append([self.tile[0] - self.color, self.tile[1] + i]) # Add the tile to the possible moves
            except:
                pass # Deal with the out of range error

        return list_possible_moves

class King:

    def __init__(self, rect, tile, color, first_move):
        self.rect = rect  # Rect of the piece's image
        self.tile = tile  # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black
        self.first_move = first_move # Usefull in pieces.possible_move()

    def update_possible_moves(self):
        from Assets import dico_board
        list_possible_moves = []
        for i in range(-1, 2): # i = -1 / 1 or 0
            for j in range(-1, 2): # j = -1 / 1 or 0
                try:
                    if (i, j) != (0,0): # If the tile is not the same as the king
                        if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]: # If the tile is empty or an opponent piece
                            list_possible_moves.append([self.tile[0] + i, self.tile[1] + j]) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error

        return list_possible_moves

class Knight:

    def __init__(self, rect, tile, color, first_move):
        self.rect = rect  # Rect of the piece's image
        self.tile = tile  # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black
        self.first_move = first_move  # Usefull in pieces.possible_move()

    def update_possible_moves(self):
        from Assets import dico_board
        list_possible_moves = []
        for i in range(-2, 3, 4): # i = -2 or 2
            for j in range(-1, 2, 2): # j = -1 or 1
                try:
                    if dico_board[(self.tile[0] + i, self.tile[1] + j)][2] in [0, - self.color]: # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] + j]) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error$
                try:
                    if dico_board[(self.tile[0] + j, self.tile[1] + i)][2] in [0, - self.color]: # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + j, self.tile[1] + i]) # Add the tile to the possible moves
                except:
                    pass # Deal with the out of range error

        return list_possible_moves

class Rook:

    def __init__(self, rect, tile, color, first_move):
        self.rect = rect  # Rect of the piece's image
        self.tile = tile  # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black
        self.first_move = first_move # Usefull in pieces.possible_move()

    def update_possible_moves(self):
        from Assets import dico_board
        list_possible_moves = []
        try:
            for i in range(1, self.tile[0] + 1): # Move above the rook piece
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == 0: # If the tile is empty
                    list_possible_moves.append([self.tile[0] - i, self.tile[1]]) # Add the tile to the possible moves
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == - self.color: # If the tile is occured by an opponent piece
                    list_possible_moves.append([self.tile[0] - i, self.tile[1]]) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0] - i, self.tile[1])][2] == self.color: # If the tile is an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error

        try:
            for i in  range(1, ROW - self.tile[0] + 1): # Move below the rook piece
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == 0: # If the tile is empty
                    list_possible_moves.append([self.tile[0] + i, self.tile[1]]) # Add the tile to the possible moves
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == - self.color: # If the tile is occured by an opponent piece
                    list_possible_moves.append([self.tile[0] + i, self.tile[1]]) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0] + i, self.tile[1])][2] == self.color: # If the tile is an ally piece
                    break # Stop the loop
        except:
            pass
        try:
            for i in range(1, self.tile[1] + 1): # Move to the left of the rook piece
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == 0: # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] - i]) # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == - self.color: # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] - i])  # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] - i)][2] == self.color: # If the tile is an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error
        try:
            for i in range(1, COL - self.tile[1] + 1): # Move to the right of the rook piece
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == 0: # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] + i]) # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == - self.color: # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] + i]) # Add the tile to the possible moves
                    break # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] + i)][2] == self.color: # If the tile is an ally piece
                    break # Stop the loop
        except:
            pass # Deal with the out of range error

        return list_possible_moves



class Bishop:

    def __init__(self, rect, tile, color, first_move):
        self.rect = rect  # Rect of the piece's image
        self.tile = tile  # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black  # -1 if white, 1 if black
        self.first_move = first_move  # Usefull in pieces.possible_move()

    def update_possible_moves(self):
        from Assets import dico_board
        list_possible_moves = []
        enter_left_down = True
        enter_left_up = True
        enter_right_up = True
        enter_right_down = True
        for i in range(1, ROW):
            try:
                if enter_left_up:
                    if dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] - i, self.tile[1] - i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] - i, self.tile[1] - i])  # Add the tile to the possible moves
                        enter_left_up = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] - i)][2] == self.color:  # If the tile is an ally piece
                        enter_left_up = False
            except:
                enter_left_up = False  # Deal with the out of range error
            try:
                if enter_left_down:
                    if dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] - i, self.tile[1] + i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] - i, self.tile[1] + i])  # Add the tile to the possible moves
                        enter_left_down = False
                    elif dico_board[(self.tile[0] - i, self.tile[1] + i)][2] == self.color:  # If the tile is an ally piece
                        enter_left_down = False
            except:
                enter_left_down = False  # Deal with the out of range error
            try:
                if enter_right_up:
                    if dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] - i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == - self.color: # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] - i])  # Add the tile to the possible moves
                        enter_right_up = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == self.color:  # If the tile is an ally piece
                        enter_right_up = False
            except:
                enter_right_up = False  # Deal with the out of range error
            try:
                if enter_right_down:
                    if dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] + i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == - self.color: # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] + i])  # Add the tile to the possible moves
                        enter_right_down = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == self.color:  # If the tile is an ally piece
                        enter_right_down = False
            except:
                enter_right_down = False  # Deal with the out of range error

        return list_possible_moves


class Queen:

    def __init__(self, rect, tile, color, first_move):
        self.rect = rect  # Rect of the piece's image
        self.tile = tile  # Tile where the pieces is
        self.color = color  # 1 if white, -1 if black
        self.first_move = first_move  # Usefull in pieces.possible_move()

    def update_possible_moves(self):
        from Assets import dico_board
        # Bishop move
        list_possible_moves = []
        enter_left_down = True
        enter_left_up = True
        enter_right_up = True
        enter_right_down = True
        for i in range(1, ROW):
            try:
                if enter_left_up:
                    new_tile = (self.tile[0] - i, self.tile[1] - i)
                    if dico_board[new_tile][2] == 0:  # If the tile is empty
                        list_possible_moves.append(list(new_tile))  # Add the tile to the possible moves
                    elif dico_board[new_tile][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(list(new_tile))  # Add the tile to the possible moves
                        enter_left_up = False
                    elif dico_board[new_tile][2] == self.color:  # If the tile is an ally piece
                        enter_left_up = False
            except:
                enter_left_up = False  # Deal with the out of range error
            try:
                if enter_left_down:
                    new_tile = (self.tile[0] - i, self.tile[1] + i)
                    if dico_board[new_tile][
                        2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(
                            list(new_tile))  # Add the tile to the possible moves
                    elif dico_board[new_tile][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(list(new_tile))  # Add the tile to the possible moves
                        enter_left_down = False
                    elif dico_board[new_tile][
                        2] == self.color:  # If the tile is an ally piece
                        enter_left_down = False
            except:
                enter_left_down = False  # Deal with the out of range error
            try:
                if enter_right_up:
                    if dico_board[(self.tile[0] + i, self.tile[1] - i)][
                        2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(
                            [self.tile[0] + i, self.tile[1] - i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append([self.tile[0] + i, self.tile[1] - i])  # Add the tile to the possible moves
                        enter_right_up = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] - i)][
                        2] == self.color:  # If the tile is an ally piece
                        enter_right_up = False
            except:
                enter_right_up = False  # Deal with the out of range error
            try:
                if enter_right_down:
                    if dico_board[(self.tile[0] + i, self.tile[1] + i)][
                        2] == 0:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(
                            [self.tile[0] + i, self.tile[1] + i])  # Add the tile to the possible moves
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][2] == - self.color:  # If the tile is empty or an opponent piece
                        list_possible_moves.append(
                            [self.tile[0] + i, self.tile[1] + i])  # Add the tile to the possible moves
                        enter_right_down = False
                    elif dico_board[(self.tile[0] + i, self.tile[1] + i)][
                        2] == self.color:  # If the tile is an ally piece
                        enter_right_down = False
            except:
                enter_right_down = False  # Deal with the out of range error

        # Rook move
        try:
            for i in range(1, self.tile[0] + 1):  # Move above the rook piece
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == 0:  # If the tile is empty
                    list_possible_moves.append([self.tile[0] - i, self.tile[1]])  # Add the tile to the possible moves
                if dico_board[(self.tile[0] - i, self.tile[1])][2] == - self.color:  # If the tile is occured by an opponent piece
                    list_possible_moves.append([self.tile[0] - i, self.tile[1]])  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0] - i, self.tile[1])][
                    2] == self.color:  # If the tile is an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error

        try:
            for i in range(1, ROW - self.tile[0] + 1):  # Move below the rook piece
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == 0:  # If the tile is empty
                    list_possible_moves.append([self.tile[0] + i, self.tile[1]])  # Add the tile to the possible moves
                if dico_board[(self.tile[0] + i, self.tile[1])][2] == - self.color:  # If the tile is occured by an opponent piece
                    list_possible_moves.append([self.tile[0] + i, self.tile[1]])  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0] + i, self.tile[1])][
                    2] == self.color:  # If the tile is an ally piece
                    break  # Stop the loop
        except:
            pass
        try:
            for i in range(1, self.tile[1] + 1):  # Move to the left of the rook piece
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == 0:  # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] - i])  # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] - i)][2] == - self.color:  # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] - i])  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] - i)][
                    2] == self.color:  # If the tile is an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error
        try:
            for i in range(1, COL - self.tile[1] + 1):  # Move to the right of the rook piece
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == 0:  # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] + i])  # Add the tile to the possible moves
                if dico_board[(self.tile[0], self.tile[1] + i)][2] == - self.color:  # If the tile is empty
                    list_possible_moves.append([self.tile[0], self.tile[1] + i])  # Add the tile to the possible moves
                    break  # Stop the loop
                elif dico_board[(self.tile[0], self.tile[1] + i)][
                    2] == self.color:  # If the tile is an ally piece
                    break  # Stop the loop
        except:
            pass  # Deal with the out of range error

        return list_possible_moves