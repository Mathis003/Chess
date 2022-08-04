from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES, pygame, white_queen_rect, white_queen_image, black_queen_image
from all_pieces import Pawn, Queen

class Pieces:

    def __init__(self, king_white, king_black):
        self.king_white = king_white
        self.king_black = king_black
        self.dico_list_pieces = {1 : LIST_WHITE_PIECES, -1 : LIST_BLACK_PIECES}

    def regroup_all_possibe_move(self, color_number):
        """ Regroup all the possible move of all the pieces of the color_number."""
        list_all_moves = []
        for piece in self.dico_list_pieces[color_number]:
            possible_move = piece.update_possible_moves()
            for move in possible_move:
                list_all_moves.append(move)
        return list_all_moves

    def CheckOwnChess(self, color_number, chess_tile):
        """Return if the move put the king in Chess."""
        list_all_moves = self.regroup_all_possibe_move(color_number)
        if chess_tile in list_all_moves:
            return True
        return False

######### CheckOwnChess in possible_move doesn't work !!!! #########
######### CheckOwnChess in possible_move doesn't work !!!! #########
######### CheckOwnChess in possible_move doesn't work !!!! #########
######### CheckOwnChess in possible_move doesn't work !!!! #########

    def possible_moves(self, piece_moved, initial_tile, last_tile_moved):

        #color_opponent = - piece_moved.color
        #if piece_moved.color == 1:
         #   king_tile = self.king_white.tile
        #if piece_moved.color == -1:
         #   king_tile = self.king_black.tile

        # Update the possible moves of the piece_moved
        list_new_moves_possible = piece_moved.update_possible_moves()
        tile_piece = dico_pieces[piece_moved][0]
        dico_board[tile_piece][3] = []  # Reset the list of possible moves of the piece
        # Move is in fact a tile which the piece can move on
        for move in list_new_moves_possible:  # Loop for each move
            #if not self.CheckOwnChess(color_opponent, king_tile):
            dico_board[tile_piece][3].append(move)  # Add the move to the list

        for i in range(-1,2,2): # If i = -1 or i = 1
            for piece in self.dico_list_pieces[i]: # Loop for each piece of the good color
                tile_piece = dico_pieces[piece][0]
                if piece.first_move:
                    list_new_moves_possible = piece.update_possible_moves()  # Update possible moves of the piece
                    dico_board[tile_piece][3] = []  # Reset the list of possible moves of the piece
                    # Move is in fact a tile which the piece can move on
                    for move in list_new_moves_possible:  # Loop for each move
                        #if not self.CheckOwnChess(color_opponent, king_tile):
                        dico_board[tile_piece][3].append(move)  # Add the move to the list
                else:
                    if last_tile_moved in dico_board[tile_piece][3] or initial_tile in dico_board[tile_piece][3]: # If the piece can move to the last_tile_moved or to the initial_tile
                        list_new_moves_possible = piece.update_possible_moves() # Update possible moves of the piece
                        dico_board[tile_piece][3] = [] # Reset the list of possible moves of the piece
                        # Move is in fact a tile which the piece can move on
                        for move in list_new_moves_possible: # Loop for each move
                            #if not self.CheckOwnChess(color_opponent, king_tile):
                            dico_board[tile_piece][3].append(move) # Add the move to the list


    def Promotion_Pawn(self, piece, new_tile):
        """ If the piece is a Pawn and move to the last line, the pawn must be promoted to a Queen => Return True."""
        if type(piece) == type(Pawn(pygame.Rect(0, 0, 0, 0), [6, 0], 1, True)):
            if piece.color == 1: # Check if the pawn is white
                if new_tile[0] == 0: # If the pawn can move to the last line on the board
                    return True
            if piece.color == -1: # Check if the pawn is black
                if new_tile[0] == 7: # If the pawn can move to the first line on the board
                    return True
        return False

    def PromotePawn_into_Queen(self, piece, new_tile):
        """Promote the pawn into a Queen"""
        if piece.color == 1: # If the piece is white
            image_queen = white_queen_image
            list_piece = LIST_WHITE_PIECES
        else:
            image_queen = black_queen_image
            list_piece = LIST_BLACK_PIECES

        new_queen = Queen(white_queen_rect, list(new_tile), piece.color, True)
        self.remove_from_list_piece_eaten(new_tile)
        # Change the object in the dictionary
        dico_board[dico_pieces[piece][0]] = [None, None, 0, []] # Reset the tile of the pawn from the dico_board
        dico_board[new_tile] = [new_queen, image_queen, piece.color, []]  # Add the queen to the dico_board
        del dico_pieces[piece] # Delete the pawn from the dico_pieces
        dico_pieces[new_queen] = [new_tile, image_queen] # Add the queen to the dico_pieces
        # Update LIST OF PIECES
        list_piece.remove(piece) # Remove the pawn from the list of pieces
        list_piece.append(new_queen) # Add the queen to the list of pieces


    def CheckChess(self, piece_moved):
        """ Detect if a piece put the king in Chess => If Chess, return the piece who put the king in Chess."""
        if piece_moved.color == 1:
            tile_king = self.king_black.tile
        if piece_moved.color == -1:
            tile_king = self.king_white.tile

        tile_piece_moved =  dico_pieces[piece_moved][0]
        if tile_king in dico_board[tile_piece_moved][3]:
            return True
        return False

    def ChessMod_update_possibles_move(self, piece_put_in_chess):
        """Update all the possible move if the king is in Chess.
        color_king_in_chess = 1 if white / -1 if black"""

        if piece_put_in_chess.color == 1:
            king_chess = self.king_black
        if piece_put_in_chess.color == -1:
            king_chess = self.king_white

        tile_piece_put_in_chess = dico_pieces[piece_put_in_chess][0]
        for piece in self.dico_list_pieces[- piece_put_in_chess.color]:
            tile_piece = dico_pieces[piece][0]
            all_possible_moves_piece = dico_board[tile_piece][3]
            for move_tile in all_possible_moves_piece:
                if tuple(move_tile) != tile_piece_put_in_chess:
                    # Check with a simulation if the piece can protect the king by moving => If not, remove the move_tile !
                    dico_board[tuple(move_tile)][2] = - piece_put_in_chess.color
                    new_list_possible_moves_piece = piece_put_in_chess.update_possible_moves()
                    if list(king_chess.tile) in new_list_possible_moves_piece:
                        dico_board[tile_piece][3].remove(move_tile)
                    dico_board[tuple(move_tile)][2] = 0

    def Check_Checkmate(self, piece_put_in_chess):
        """ Check if the king is in Checkmate => If Checkmate, return True to end the game."""
        for piece in self.dico_list_pieces[- piece_put_in_chess.color]:
            tile_piece = dico_pieces[piece][0]
            if dico_board[tile_piece][3] != []:
                return False
        return True


    def remove_from_list_piece_eaten(self, new_tile):
        # Remove the object (in the pieces list) from the old tile
        if dico_board[new_tile][0] != None: # If the tile contain a piece (= isn't empty)
            if dico_board[new_tile][2] == 1: # If the piece is white
                LIST_WHITE_PIECES.remove(dico_board[new_tile][0]) # Remove the white piece from the list of pieces
            elif dico_board[new_tile][2] == -1: # If the piece is black
                LIST_BLACK_PIECES.remove(dico_board[new_tile][0]) # Remove the black piece from the list of pieces
            del dico_pieces[dico_board[new_tile][0]] # Remove the piece eaten from the dico_pieces

    def update_dico_pieces(self, piece, new_tile):
        # Update the position of the piece_image on the board (which tile)
        dico_pieces[piece][0] = new_tile

    def update_dico_board(self, piece, current_tile, new_tile):
        # Update dico_moves_pieces to change the object's tile to the new tile
        dico_board[new_tile][0] = piece
        dico_board[current_tile][0] = None

        # Update dico_pieces_images_on_board to change the piece's image on the board
        dico_board[new_tile][1] = dico_board[current_tile][1]
        dico_board[current_tile][1] = None

        # Update dico_board to change the letter of the piece on the board
        dico_board[new_tile][2] = dico_board[current_tile][2]
        dico_board[current_tile][2] = 0

        # Reset the list of possible moves of the piece => it will be updated again in the next turn
        dico_board[new_tile][3] = []
        dico_board[current_tile][3] = []

    def move_piece(self, piece, current_tile, new_tile):
        self.remove_from_list_piece_eaten(new_tile)
        self.update_dico_pieces(piece, new_tile)
        self.update_dico_board(piece, current_tile, new_tile)
        # Update position of the piece on the board => piece.tile = new_tile
        piece.tile = new_tile

        if piece.first_move == True: # If the pawn is on its first move
            piece.first_move = False # The pawn is not on its first move anymore