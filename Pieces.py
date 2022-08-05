from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES, pygame, white_queen_rect, white_queen_image, black_queen_image
from all_pieces import Pawn, Queen

class Pieces:

    def __init__(self, king_white, king_black):
        self.king_white = king_white
        self.king_black = king_black
        self.dico_list_pieces = {1 : LIST_WHITE_PIECES, -1 : LIST_BLACK_PIECES}

    def King_ownChess(self, king_piece, move_tile):
        l_remove_from_list = []
        save_color_case = dico_board[tuple(move_tile)][2]
        dico_board[tuple(move_tile)][2] = 0
        for piece in self.dico_list_pieces[- king_piece.color]:
            new_list_possible_moves = piece.update_possible_moves()
            if move_tile in new_list_possible_moves:
                l_remove_from_list.append(move_tile)
                break

        dico_board[tuple(move_tile)][2] = save_color_case
        print(l_remove_from_list)
        return l_remove_from_list


    def CheckOwnChess_pieces(self, own_piece, king_tile):
        """Return if the own move put the king in Chess."""
        for piece in self.dico_list_pieces[- own_piece.color]:
            if own_piece.tile in dico_board[dico_pieces[piece][0]][3]:

                if type(own_piece) != type(self.king_white): # If the piece is not the king
                    # Simu
                    save_possible_moves_piece = dico_board[dico_pieces[piece][0]][3]
                    save_color_piece = dico_board[dico_pieces[own_piece][0]][2]
                    dico_board[dico_pieces[own_piece][0]][2] = 0
                    new_list_possible_moves = piece.update_possible_moves()
                    if king_tile in new_list_possible_moves:
                        dico_board[dico_pieces[own_piece][0]][3] = []
                    else:
                        dico_board[dico_pieces[piece][0]][3] = save_possible_moves_piece
                    dico_board[dico_pieces[own_piece][0]][2] = save_color_piece
                else: # If the piece is the king

                    all_possible_moves_piece = dico_board[tuple(own_piece.tile)][3]
                    l_to_remove_move_tile = []

                    # See if the king can move to ESCAPE
                    dico_board[tuple(own_piece.tile)][2] = 0
                    for move_tile in all_possible_moves_piece:
                        # Check with a simulation if the king can escape by moving => If not, remove the move_tile !
                        # Changes for the simu
                        save_color_tile = dico_board[tuple(move_tile)][2]
                        dico_board[tuple(move_tile)][2] = own_piece.color
                        # Check the simu
                        new_list_possible_moves_piece = piece.update_possible_moves()
                        if move_tile in new_list_possible_moves_piece:
                            l_to_remove_move_tile.append(move_tile)
                        # Reset
                        dico_board[tuple(own_piece.tile)][2] = own_piece.color
                        dico_board[tuple(move_tile)][2] = save_color_tile

                    # Remove the move_tile from the list of possible move of the piece (if necessary)
                    for move_tile in l_to_remove_move_tile:
                        dico_board[tuple(own_piece.tile)][3].remove(move_tile)



    def possible_moves(self, piece_moved, initial_tile, last_tile_moved):
        """Update the basics possible moves of the pieces."""
        for i in range(-1,2,2): # If i = -1 or i = 1
            for piece in self.dico_list_pieces[i]: # Loop for each piece of the good color
                tile_piece = dico_pieces[piece][0]
                dico_board[tile_piece][3] = piece.update_possible_moves()  # Update possible moves of the piece


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

        tile_piece_moved = dico_pieces[piece_moved][0]
        if tile_king in dico_board[tile_piece_moved][3]:
            return True
        return False

    def UpdateKingMoves(self, piece_moved):
        if piece_moved.color == 1:
            king_chess = self.king_black
        if piece_moved.color == -1:
            king_chess = self.king_white

        l_to_remove_move_tile = []
        for move_tile in dico_board[tuple(king_chess.tile)][3]:
            dico_board[tuple(king_chess.tile)][2] = 0
            save_color_case = dico_board[tuple(move_tile)][2]
            dico_board[tuple(move_tile)][2] = king_chess.color
            for piece in self.dico_list_pieces[piece_moved.color]:
                new_all_possible_moves = piece.update_possible_moves()
                if move_tile in new_all_possible_moves:
                    l_to_remove_move_tile.append(move_tile)
                    dico_board[tuple(move_tile)][2] = save_color_case
                    break
            dico_board[tuple(move_tile)][2] = save_color_case

        dico_board[tuple(king_chess.tile)][2] = king_chess.color
        # Remove the move_tile from the list of possible move of the piece (if necessary)
        for move_tile in l_to_remove_move_tile:
            dico_board[tuple(king_chess.tile)][3].remove(move_tile)


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
            l_to_remove_move_tile = []
            if type(piece) == type(self.king_white): # If the piece is the king
                self.UpdateKingMoves(piece_put_in_chess)

            else: # If the piece is not the king
                # See if the piece can move to PROTECT the king
                for move_tile in all_possible_moves_piece:
                    if tuple(move_tile) != tile_piece_put_in_chess:
                        # Check with a simulation if the piece can protect the king by moving => If not, remove the move_tile !
                        dico_board[tuple(move_tile)][2] = - piece_put_in_chess.color
                        new_list_possible_moves_piece = piece_put_in_chess.update_possible_moves()
                        if king_chess.tile in new_list_possible_moves_piece:
                            l_to_remove_move_tile.append(move_tile)
                        dico_board[tuple(move_tile)][2] = 0
                # Remove the move_tile from the list of possible move of the piece
                for move_tile in l_to_remove_move_tile:
                    dico_board[tile_piece][3].remove(move_tile)

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
        piece.tile = list(new_tile)

        if piece.first_move == True: # If the pawn is on its first move
            piece.first_move = False # The pawn is not on its first move anymore