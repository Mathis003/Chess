from src.all_pieces import Pawn, King, Piece, dico_board, dico_list_pieces

class Pieces:

    def __init__(self, king_white, king_black):
        self.piece = Piece(None, None, None)
        self.king_white = king_white
        self.king_black = king_black

### Function very usefull for the paragraph just below ###

    def King_with_his_Tile(self, piece_moved):
        """
        :param piece_moved: piece that just moved
        :return: a tuple : the opponent king piece ('opponent' compared to piece_moved), tile of this king
        """
        """Return the king piece and his tile (opponent to the piece moved)."""
        king, tile_king = None, None
        if piece_moved.color == 1:
            king, tile_king = self.king_black, self.king_black.tile
        if piece_moved.color == -1:
            king, tile_king = self.king_white, self.king_white.tile
        return king, tile_king



###########################################################
### Function to have all the possibles moves with all the possible case => prevent Check,... ###

    ### IMPORTANT FUNCTION !!! ###

    def basics_possible_moves(self, moved_piece):
        """
        Update the dico_board with the basics possible moves of the pieces + specials moves of pawn and king.
        :param moved_piece: piece that just moved
        """
        for piece in dico_list_pieces[- moved_piece.color]: # Loop for each piece of the good color
            dico_board[piece.tile][3] = piece.update_possible_moves()  # Update possible moves of the piece

            if isinstance(piece, type(King((7, 4), 1, True, 0, 0))): # If the piece is the king
                piece.castling_stroke() # Update the possible moves of the king if he can do the "Castling" stroke

            if isinstance(piece, type(Pawn((7, 4), 1, True))): # If the piece is the pawn
                possible_move = piece.move_en_passant()
                # If the pawn can do the "en passant" move
                if len(possible_move) != 0:
                    # Update the possible moves of the pawn by adding the move(s) "en passant"
                    for move_tile in possible_move:
                        dico_board[piece.tile][3].append(move_tile)

    def PieceTouchPieceMoved(self, current_tile, color_piece_to_analyse):
        """
        :param current_tile: tile of the piece_moved before her move
        :param color_piece_to_analyse: color of piece_moved
        :return: list of pieces that can hit the current_tile if the piece_moved move (pieces must have the same color
                 than the piece_moved's color)
        """
        list_pieces = []
        for piece in dico_list_pieces[color_piece_to_analyse]:
            new_possible_moves = piece.update_possible_moves()
            if current_tile in new_possible_moves:
                list_pieces.append(piece)
        return list_pieces

    ### IMPORTANT FUNCTION !!! ###

    def CheckOpponent(self, piece_moved, current_tile):
        """
        Check if the opponent is in check => in this case, boolean = True, piece = piece that put the king in check.
        Otherwise, boolean = False and piece = None.
        :param piece_moved: piece that just moved
        :param current_tile: tile of the piece_moved before her move
        :return: boolean, piece
        """
        """Check if the opponent is in check => return True, False otherwise."""
        tile_king = self.King_with_his_Tile(piece_moved)[1]
        list_pieces_to_test = self.PieceTouchPieceMoved(current_tile, piece_moved.color) # Get the list of pieces that are touching the piece moved
        if piece_moved not in list_pieces_to_test:
            list_pieces_to_test.append(piece_moved) # Add the piece moved to the list of pieces to test

        for piece in list_pieces_to_test: # Loop for each piece of the list
            new_list_possible_moves = piece.update_possible_moves() # Update the possible moves of the piece moved
            if tile_king in new_list_possible_moves:
                return True, piece
        return False, None

    ### IMPORTANT FUNCTION !!! ###

    def Check_NoMoveAvailable(self, piece_moved):
        """
        Check if the opponent has no possible move at all => in this case, boolean = True.
        Otherwise, boolean = False.
        :param piece_moved: piece that just moved
        :return: boolean
        """
        """Check if the king is in checkmate."""
        for piece in dico_list_pieces[- piece_moved.color]:
            if dico_board[piece.tile][3] != []:
                return False
        return True

    ### IMPORTANT FUNCTION !!! ###

    def ReUpdate_ToNot_OwnChess(self, piece_moved):
        """
        Update the dico_board with the possible moves for the opponent => To not put the king himself in check (or checkmate)
        or to not play an other piece that put the king in check (or checkmate).
        :param piece_moved: piece that just moved
        """
        for piece in dico_list_pieces[- piece_moved.color]: # Loop for each piece of the good color
            if isinstance(piece, type(King([7, 4], 1, True, 0, 0))): # If the piece is the king
                self.UpdateKingMoves_ToNotBeInCheck(piece_moved)
            else: # If the piece is not the king
                self.UpdatePiecesMoves_ToNotPutKingInCheck(piece, piece_moved)

    def UpdateKingMoves_ToNotBeInCheck(self, piece_moved):
        """
        Update the dico_board with the possible moves of the king so he can't put himself in check (or checkmate).
        :param piece_moved: piece that just moved
        """
        king_chess = self.King_with_his_Tile(piece_moved)[0]  # Get the king's piece (opponent to the piece moved)
        l_to_remove_move_tile = []
        for move_tile in dico_board[king_chess.tile][3]: # Loop for each possible move of the king
            dico_board[king_chess.tile][2] = 0 # Simulate that the king isn't there
            save_color_tile = dico_board[move_tile][2] # Save the color of the tile's moved
            dico_board[move_tile][2] = king_chess.color # Simulate that the king is there
            for piece in dico_list_pieces[piece_moved.color]: # Loop for each piece of the opponent color
                new_all_possible_moves = piece.update_possible_moves() # Update possible moves of the piece
                if move_tile in new_all_possible_moves: # If the king is also in Check here
                    l_to_remove_move_tile.append(move_tile) # Add the move tile to the list of move tile to remove
                    dico_board[move_tile][2] = save_color_tile # Reset the color of the tile's moved
                    break # Break the loop for each piece of the opponent color => to change the move tiled
            dico_board[move_tile][2] = save_color_tile # Reset the color of the tile's moved

        dico_board[king_chess.tile][2] = king_chess.color # Reset the color of the tile's king
        # Remove the move_tile from the list of possible move of the piece (if necessary)
        for move_tile in l_to_remove_move_tile: # Loop for each move tile to remove
            dico_board[king_chess.tile][3].remove(move_tile) # Remove the move tile from the list of possible moves of the king

    def UpdatePiecesMoves_ToNotPutKingInCheck(self, piece, piece_moved):
        """
        Update the dico_board with the possible moves of the piece so she can't put the king in check (or checkmate).
        :param piece: piece to analyse and potentially update his possible moves
        :param piece_moved: piece that just moved
        """
        l_to_remove_from_the_list = []
        list_possible_moves = piece.update_possible_moves()  # Update possible moves of the piece
        tile_king = self.King_with_his_Tile(piece_moved)[1]
        if list_possible_moves != []:
            list_piece = self.PieceTouchPieceMoved(piece.tile, piece_moved.color)
            dico_board[piece.tile][2] = 0  # Simulate that the piece isn't there to see if the piece protect the king (being there) or not
            for piece_touch in list_piece:
                new_list_possible_moves = piece_touch.update_possible_moves()
                if tile_king in new_list_possible_moves:
                    for move_tile in list_possible_moves:
                        if move_tile != piece_touch.tile:
                            save_color_tile = dico_board[move_tile][2]
                            dico_board[move_tile][2] = piece.color
                            new_list_possible_moves = piece_touch.update_possible_moves()
                            if tile_king in new_list_possible_moves:
                                l_to_remove_from_the_list.append(move_tile)
                            dico_board[move_tile][2] = save_color_tile

            dico_board[piece.tile][2] = piece.color  # Reset the color tile
            for move_tile_to_remove in l_to_remove_from_the_list:
                dico_board[piece.tile][3].remove(move_tile_to_remove)

    ### IMPORTANT FUNCTION !!! ###

    def CheckMod_reupdate_possibles_move(self, piece_that_check):
        """
        ReUpdate all the possible move if the king is in Chess => Only the pieces which can protect the king could
        play at these tiles ! and the king himself if he can escappe without putting himself AGAIN in check (or checkmate).
        :param piece_that_check: piece that put the opponent king in check
        """
        king_check = self.King_with_his_Tile(piece_that_check)[0] # Get the king's piece (opponent to the piece moved)
        for piece in dico_list_pieces[king_check.color]: # Loop for each piece of the king's color
            if isinstance(piece, type(self.king_white)): # If the piece is the king
                self.UpdateKingMoves_ToNotBeInCheck(piece_that_check) # Update the possible moves of the king BEING in check!
            else: # If the piece is not the king
                self.ReupdatePossibleMoves_ToProtectKing(piece_that_check, piece, king_check)

    def ReupdatePossibleMoves_ToProtectKing(self, piece_that_check, piece, king_check):
        """
        ReUpdate the possible moves of the 'piece' => Keep only the tile where the piece can protect the king.
        :param piece_that_check: piece that put the opponent king in check
        :param piece: piece to analyse his possible moves
        :param king_check: king which is in check
        """
        all_possible_moves_piece = dico_board[piece.tile][3]  # Get the possible moves of the piece
        l_to_remove_move_tile = []
        if not self.IfPieceMove_CheckAgain(piece_that_check, piece, king_check):
            # See if the piece can move to PROTECT the king
            for move_tile in all_possible_moves_piece:  # Loop for each possible move of the piece
                if move_tile != piece_that_check.tile:
                    # Check with a simulation if the piece can protect the king by moving => If not, remove the move_tile !
                    save_color_tile = dico_board[move_tile][2]
                    dico_board[move_tile][2] = - piece_that_check.color  # Simulate that the piece move to see if the piece protect the king (being there) or not
                    new_list_possible_moves_piece = piece_that_check.update_possible_moves()  # Update possible moves of the piece who put the king in check
                    if king_check.tile in new_list_possible_moves_piece:  # If the piece doesn't protect the king
                        l_to_remove_move_tile.append(move_tile)  # Add to the list to remove all the move that doesn't protect the king
                    dico_board[move_tile][2] = save_color_tile  # Reset the color of the tile

            # Remove the move_tile from the list of possible move of the piece
            for move_tile in l_to_remove_move_tile:
                dico_board[piece.tile][3].remove(move_tile)

    def IfPieceMove_CheckAgain(self, piece_that_check, piece, king_check):
        """
        Simulate and test if when the 'piece' move, the king is check by another piece than 'piece_that_check'.
        If the king always checked => boolean enter = True.
        Otherwise, boolean enter = False.
        :param piece_that_check: piece that put the opponent king in check
        :param piece to analyse his possible moves
        :param king_check: king which is in check
        :return: boolean for an enter
        """
        enter = False
        dico_board[piece.tile][2] = 0  # Simulate that the piece isn't there to see if another opponent piece put the king in check
        for opponent_piece in dico_list_pieces[piece_that_check.color]:
            if opponent_piece != piece_that_check:  # If the piece is not the piece that check the king
                new_all_possible_moves = opponent_piece.update_possible_moves()  # Update possible moves of the piece
                if king_check.tile in new_all_possible_moves:  # If the king is in check here
                    dico_board[piece.tile][3] = []  # Reset the possible moves of the piece
                    enter = True
                    break

        dico_board[piece.tile][2] = piece.color  # Reset the color of the tile
        return enter