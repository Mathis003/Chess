from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES
from all_pieces import King

class Pieces:

    def __init__(self, king_white, king_black):
        self.king_white = king_white
        self.king_black = king_black
        self.dico_list_pieces = {1 : LIST_WHITE_PIECES, -1 : LIST_BLACK_PIECES}

    def possible_moves(self):
        for i in range(-1,2,2): # If i = -1 or i = 1
            for piece in self.dico_list_pieces[i]: # Loop for each piece
                tile_piece = dico_pieces[piece][0]
                list_new_moves_possible = piece.update_possible_moves() # Update possible moves of the piece
                # Move is in fact a tile which the piece can move on
                for move in list_new_moves_possible: # Loop for each move
                    if move not in dico_board[tile_piece][3]: # If the move isn't in the list
                        dico_board[tile_piece][3].append(move) # Add the move to the list

    def CheckSquare(self):
        """
        Detect if a piece put the king in Chess
        => If Chess, return the piece who put the king in Chess.
        """
        tile_king_white = self.king_white.tile
        tile_king_black = self.king_black.tile
        for i in range(-1,2,2): # If i = -1 or i = 1
            for piece in self.dico_list_pieces[i]:
                tile_piece = dico_pieces[piece][0]
                all_possible_moves_piece = dico_board[tile_piece][3]
                for move_tile in all_possible_moves_piece:
                    if i == 1:
                        if tuple(move_tile) == tile_king_black:
                            return piece
                    if i == -1:
                        if tuple(move_tile) == tile_king_white:
                            return piece
        return None

    def ChessMod_update_possibles_move(self, king_chess, piece_put_in_chess):
        """Update all the possible move if the king is in Chess.
        color_king_in_chess = 1 if white / -1 if black"""
        tile_piece_put_in_chess = dico_pieces[piece_put_in_chess][0]
        for piece in self.dico_list_pieces[king_chess.color]:
            tile_piece = dico_pieces[piece][0]
            all_possible_moves_piece = dico_board[tile_piece][3]
            for move_tile in all_possible_moves_piece:
                if tuple(move_tile) != tile_piece_put_in_chess:
                    # Check with a simulation if the piece can protect the king by moving => If not, remove the move_tile !
                    dico_board[tuple(move_tile)][2] = king_chess.color
                    new_list_possible_moves_piece = piece_put_in_chess.update_possible_moves()
                    if list(king_chess.tile) in new_list_possible_moves_piece:
                        dico_board[tile_piece][3].remove(move_tile)
                    dico_board[tuple(move_tile)][2] = 0

    def remove_from_list_piece_eaten(self, new_tile):
        # Remove the object (in the pieces list) from the old tile
        if dico_board[new_tile][0] != None: # If the tile contain a piece (= isn't empty)
            if dico_board[new_tile][2] == 1: # If the piece is white
                LIST_WHITE_PIECES.remove(dico_board[new_tile][0]) # Remove the white piece from the list of pieces
            elif dico_board[new_tile][2] == -1: # If the piece is black
                LIST_BLACK_PIECES.remove(dico_board[new_tile][0]) # Remove the black piece from the list of pieces

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
        try: # If the piece is a pawn
            if piece.first_move == True: # If the pawn is on its first move
                piece.first_move = False # The pawn is not on its first move anymore
        except:
            pass # If the piece is not a pawn