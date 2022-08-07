import math
import random
import time

from Assets import dico_board, LIST_BLACK_PIECES, LIST_WHITE_PIECES, white_queen_image, black_queen_image,\
    matrix_points_pawn_white, matrix_points_pawn_black, matrix_points_bishop_white, matrix_points_bishop_black,\
    matrix_points_knight_white, matrix_points_knight_black, matrix_points_rook_white, matrix_points_rook_black,\
    matrix_points_queen_white, matrix_points_queen_black, matrix_points_king_white, matrix_points_king_black
from all_pieces import Pawn, Queen, King, Bishop, Knight, Rook

class Pieces:

    def __init__(self, king_white, king_black):
        self.king_white = king_white
        self.king_black = king_black
        self.dico_list_pieces = {1 : LIST_WHITE_PIECES, -1 : LIST_BLACK_PIECES}
        self.dico_points_pieces_white = {type(Pawn((7, 4), 1, True)) : matrix_points_pawn_white,
                                         type(Queen((7, 4), 1, True)) : matrix_points_queen_white,
                                         type(King((7, 4), 1, True, 0, 0)) : matrix_points_king_white,
                                         type(Bishop((7, 4), 1, True)) : matrix_points_bishop_white,
                                         type(Knight((7, 4), 1, True)) : matrix_points_knight_white,
                                         type(Rook((7, 4), 1, True)) : matrix_points_rook_white}

        self.dico_points_pieces_black = {type(Pawn((7, 4), 1, True)): matrix_points_pawn_black,
                                         type(Queen((7, 4), 1, True)): matrix_points_queen_black,
                                         type(King((7, 4), 1, True, 0, 0)): matrix_points_king_black,
                                         type(Bishop((7, 4), 1, True)): matrix_points_bishop_black,
                                         type(Knight((7, 4), 1, True)): matrix_points_knight_black,
                                         type(Rook((7, 4), 1, True)): matrix_points_rook_black}

    def TileBetweenEmpty(self, list_tile):
        """Check if the tiles in the "list_tile" are all empty => return True, False otherwise."""
        for tile in list_tile:
            if dico_board[tile][2] != 0:
                return False
        return True

    def ChessTileBetween(self, list_tile, king_piece):
        """Check if the tiles in the "list_tile" are all not in Check => return True, False otherwise."""
        list_tile.append((7, 4))
        for piece in self.dico_list_pieces[- king_piece.color]:
            list_possible_moves = piece.update_possible_moves()
            for tile in list_tile:
                if tile in list_possible_moves:
                    return True
        return False

    def CastlingStroke(self, king_piece):
        if king_piece.color == 1: # If the king is white
            list_tile_leftstroke = [(7, 5), (7, 6)]
            list_tile_rightstroke = [(7, 3), (7, 2), (7, 1)]
            tile_to_append_left = (7, 6)
            tile_to_append_right = (7, 2)
        else: # If the king is black
            list_tile_leftstroke = [(0, 5), (0, 6)]
            list_tile_rightstroke = [(0, 3), (0, 2), (0, 1)]
            tile_to_append_left = (0, 6)
            tile_to_append_right = (0, 2)

        if king_piece.Rook_LeftStroke(): # If the king and the left rook haven't played yet
            if self.TileBetweenEmpty(list_tile_leftstroke) and not self.ChessTileBetween(list_tile_leftstroke, king_piece): # If the tiles between the king and the left rook are empty and not in check
                dico_board[king_piece.tile][3].append(tile_to_append_left) # Add the tile to the list of possible moves of the king
        if king_piece.Rook_RightStroke(): # If the king and the right rook haven't played yet
            if self.TileBetweenEmpty(list_tile_rightstroke) and not self.ChessTileBetween(list_tile_rightstroke, king_piece): # If the tiles between the king and the right rook are empty and not in check
                dico_board[king_piece.tile][3].append(tile_to_append_right) # Add the tile to the list of possible moves of the king

    def basics_possible_moves(self, moved_piece):
        """Update the basics possible moves of the pieces + specials moves."""
        for piece in self.dico_list_pieces[- moved_piece.color]: # Loop for each piece of the good color
            dico_board[piece.tile][3] = piece.update_possible_moves()  # Update possible moves of the piece

            if isinstance(piece, type(King((7, 4), 1, True, 0, 0))): # If the piece is the king
                self.CastlingStroke(piece) # Update the possible moves of the king if he can do the "Castling" stroke

            if isinstance(piece, type(Pawn((7, 4), 1, True))): # If the piece is the pawn
                enter, possible_move = piece.EnPassantMove()
                if enter: # If the pawn can do the "en passant" move
                    # Update the possible moves of the pawn by adding the move(s) "en passant"
                    for move_tile in possible_move:
                        dico_board[piece.tile][3].append(move_tile)

    def King_with_his_Tile(self, piece_moved):
        """Return the king piece and his tile (opponent to the piece moved)."""
        if piece_moved.color == 1:
            king, tile_king = self.king_black, self.king_black.tile
        if piece_moved.color == -1:
            king, tile_king = self.king_white, self.king_white.tile
        return king, tile_king

    def PieceTouchPieceMoved(self, current_tile, color_piece_to_analyse):
        """Return the list of pieces (the same color than the piece moved one) that are touching the piece moved if she moves."""
        list_pieces = []
        for piece in self.dico_list_pieces[color_piece_to_analyse]:
            new_possible_moves = piece.update_possible_moves()
            if current_tile in new_possible_moves:
                list_pieces.append(piece)
        return list_pieces

    def CheckOpponent(self, piece_moved, current_tile):
        """Check if the opponent is in check => return True, False otherwise."""
        tile_king = self.King_with_his_Tile(piece_moved)[1]
        list_pieces_to_test = self.PieceTouchPieceMoved(current_tile, - piece_moved.color) # Get the list of pieces that are touching the piece moved
        if piece_moved not in list_pieces_to_test:
            list_pieces_to_test.append(piece_moved) # Add the piece moved to the list of pieces to test

        for piece in list_pieces_to_test: # Loop for each piece of the list
            new_list_possible_moves = piece.update_possible_moves() # Update the possible moves of the piece moved
            if tile_king in new_list_possible_moves:
                return True, piece
        return False, None

    def ReUpdate_ToNot_OwnChess(self, piece_moved):
        for piece in self.dico_list_pieces[- piece_moved.color]: # Loop for each piece of the good color
            if isinstance(piece, type(King([7, 4], 1, True, 0, 0))): # If the piece is the king
                self.UpdateKingMoves_ToNotBeInCheck(piece_moved)
            else: # If the piece is not the king
                self.UpdatePiecesMoves_ToNotPutKingInCheck(piece, piece_moved)

    def UpdatePiecesMoves_ToNotPutKingInCheck(self, piece, piece_moved):
        l_to_remove_from_the_list = []
        list_possible_moves = piece.update_possible_moves()  # Update possible moves of the piece
        tile_king = self.King_with_his_Tile(piece_moved)[1]
        if list_possible_moves != []:
            list_piece = self.PieceTouchPieceMoved(piece.tile, piece_moved.color)
            dico_board[piece.tile][2] = 0  # Simulate that the piece isn't there to see if the piece protect the king (being there) or not
            if piece == dico_board[(3, 3)][0]:
                print(list_piece)
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

    def UpdateKingMoves_ToNotBeInCheck(self, piece_moved):
        """Update the possible moves of the king if he is in check."""
        king_chess = self.King_with_his_Tile(piece_moved)[0]  # Get the king's piece (opponent to the piece moved)
        l_to_remove_move_tile = []
        for move_tile in dico_board[king_chess.tile][3]: # Loop for each possible move of the king
            dico_board[king_chess.tile][2] = 0 # Simulate that the king isn't there
            save_color_tile = dico_board[move_tile][2] # Save the color of the tile's moved
            dico_board[move_tile][2] = king_chess.color # Simulate that the king is there
            for piece in self.dico_list_pieces[piece_moved.color]: # Loop for each piece of the opponent color
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

    def IfPieceMove_CheckAgain(self, piece_that_check, piece, king_chess):
        enter = True
        for opponent_piece in self.dico_list_pieces[piece_that_check.color]:
            if opponent_piece != piece_that_check:  # If the piece is not the piece that check the king
                dico_board[piece.tile][
                    2] = 0  # Simulate that the piece isn't there to see if another opponent piece put the king in check
                new_all_possible_moves = opponent_piece.update_possible_moves()  # Update possible moves of the piece
                if king_chess.tile in new_all_possible_moves:  # If the king is in check here
                    dico_board[piece.tile][3] = []  # Reset the possible moves of the piece
                    enter = False
                    dico_board[piece.tile][2] = piece.color  # Reset the color of the tile
                    break
        dico_board[piece.tile][2] = piece.color  # Reset the color of the tile
        return enter

    def ReupdatePossibleMoves_ToProtectKing(self, piece_that_check, piece, king_chess):
        all_possible_moves_piece = dico_board[piece.tile][3]  # Get the possible moves of the piece
        l_to_remove_move_tile = []
        if self.IfPieceMove_CheckAgain(piece_that_check, piece, king_chess):
            # See if the piece can move to PROTECT the king
            for move_tile in all_possible_moves_piece:  # Loop for each possible move of the piece
                if move_tile != piece_that_check.tile:
                    # Check with a simulation if the piece can protect the king by moving => If not, remove the move_tile !
                    save_color_tile = dico_board[move_tile][2]
                    dico_board[move_tile][
                        2] = - piece_that_check.color  # Simulate that the piece move to see if the piece protect the king (being there) or not
                    new_list_possible_moves_piece = piece_that_check.update_possible_moves()  # Update possible moves of the piece who put the king in check
                    if king_chess.tile in new_list_possible_moves_piece:  # If the piece doesn't protect the king
                        l_to_remove_move_tile.append(
                            move_tile)  # Add to the list to remove all the move that doesn't protect the king
                    dico_board[move_tile][2] = save_color_tile  # Reset the color of the tile

            # Remove the move_tile from the list of possible move of the piece
            for move_tile in l_to_remove_move_tile:
                dico_board[piece.tile][3].remove(move_tile)

    def CheckMod_reupdate_possibles_move(self, piece_that_check):
        """Update all the possible move if the king is in Chess."""

        king_chess = self.King_with_his_Tile(piece_that_check)[0] # Get the king's piece (opponent to the piece moved)
        for piece in self.dico_list_pieces[king_chess.color]: # Loop for each piece of the king's color
            if isinstance(piece, type(self.king_white)): # If the piece is the king
                self.UpdateKingMoves_ToNotBeInCheck(piece_that_check) # Update the possible moves of the king BEING in check!
            else: # If the piece is not the king
                self.ReupdatePossibleMoves_ToProtectKing(piece_that_check, piece, king_chess)

    def Check_Checkmate(self, piece_moved):
        """Check if the king is in checkmate."""
        for piece in self.dico_list_pieces[- piece_moved.color]:
            if dico_board[piece.tile][3] != []:
                return False
        return True

    def remove_from_list_piece_eaten(self, tile):
        # Remove the object (in the pieces list) from the old tile
        if dico_board[tile][0] != None: # If the tile contain a piece (= isn't empty)
            if dico_board[tile][2] == 1: # If the piece is white
                LIST_WHITE_PIECES.remove(dico_board[tile][0]) # Remove the white piece from the list of pieces
                self.dico_list_pieces[1] = LIST_WHITE_PIECES # Update the list of pieces
            elif dico_board[tile][2] == -1: # If the piece is black
                LIST_BLACK_PIECES.remove(dico_board[tile][0]) # Remove the black piece from the list of pieces
                self.dico_list_pieces[-1] = LIST_BLACK_PIECES  # Update the list of pieces

            if isinstance(dico_board[tile][0], type(Queen((5,5), 1, True))): # If the piece is a queen
                if dico_board[tile][2] == 1: # If the piece is white
                    pass
                elif dico_board[tile][2] == -1: # If the piece is black
                    pass

    def add_from_list_piece(self, piece):
        if piece.color == 1:
            LIST_WHITE_PIECES.append(piece)
            self.dico_list_pieces[1] = LIST_WHITE_PIECES
        elif piece.color == -1:
            LIST_BLACK_PIECES.append(piece)
            self.dico_list_pieces[-1] = LIST_BLACK_PIECES

    def update_dico_board_basic_stroke(self, piece, current_tile, new_tile):
        # Update dico_board
        dico_board[new_tile] = [piece, dico_board[current_tile][1], dico_board[current_tile][2], []]
        dico_board[current_tile] = [None, None, 0, []]

    def move_pawn(self, pawn_piece, current_tile, new_tile):
        # Promotion if the pawn can be promoted
        if new_tile[0] in [0, 7]:
            if pawn_piece.color == 1:  # Check if the pawn is white
                list_piece, image_queen = LIST_WHITE_PIECES, white_queen_image
            else:
                list_piece, image_queen = LIST_BLACK_PIECES, black_queen_image

            new_queen = Queen(new_tile, pawn_piece.color, False)
            self.remove_from_list_piece_eaten(new_tile)
            self.remove_from_list_piece_eaten(current_tile)
            self.add_from_list_piece(new_queen)  # Add the queen to the list of pieces
            # Change the object in the dictionary
            dico_board[current_tile] = [None, None, 0, []]  # Reset the tile of the pawn from the dico_board
            dico_board[new_tile] = [new_queen, image_queen, new_queen.color, []]  # Add the queen to the dico_board
            # Update the variables promoted
            new_queen.promoted = True
        else:
            # Stroke "En Passant"
            if dico_board[new_tile][2] == 0:  # If the piece is a pawn that move to an empty tile
                if new_tile == (current_tile[0] - pawn_piece.color, current_tile[1] + 1) or new_tile == (current_tile[0] - pawn_piece.color, current_tile[1] - 1):  # If the pawn move to an empty tile to eat an opponent piece ("En Passant")
                    tile_piece_eaten = (current_tile[0], new_tile[1])
                    piece_eaten = dico_board[tile_piece_eaten][0]
                    # Update the list of pieces (remove the piece eaten)
                    self.dico_list_pieces[- pawn_piece.color].remove(piece_eaten)
                    # Update dico_board
                    dico_board[tile_piece_eaten] = [None, None, 0, []]

                self.update_dico_board_basic_stroke(pawn_piece, current_tile, new_tile)

                # Update variable for the first move of the pawn abd the 'just_moved' variable
                if pawn_piece.first_move:  # If the pawn is on his first move, it can move 2 tiles
                    if abs(current_tile[0] - new_tile[0]) == 2:  # If the pawn has moved 2 tiles
                        pawn_piece.just_moved = True
                else:  # If the pawn is not on his first move anymore
                    pawn_piece.just_moved = False
            else:
                self.remove_from_list_piece_eaten(new_tile)  # Remove the piece eaten from the list of pieces (if there is one)
                self.update_dico_board_basic_stroke(pawn_piece, current_tile, new_tile)

    def move_king(self, king_piece, current_tile, new_tile):
        if king_piece.first_move:  # If the king is on his first move
            if new_tile == (7, 6):  # Right Castling
                # Update dico_board for the special stroke "Right Castling"
                dico_board[(7, 6)] = [dico_board[(7, 4)][0], dico_board[(7, 4)][1], dico_board[(7, 4)][2], []]
                dico_board[(7, 4)] = [None, None, 0, []]
                dico_board[(7, 5)] = [dico_board[(7, 7)][0], dico_board[(7, 7)][1], dico_board[(7, 7)][2], []]
                dico_board[(7, 7)] = [None, None, 0, []]
                rook_piece = dico_board[(7, 5)][0]
                rook_piece.tile = (7, 5)  # Update the rook's tile
                rook_piece.first_move = False  # The rook has moved

            elif new_tile == (7, 2):  # Left Castling
                # Update dico_board for the special stroke "Left Castling"
                dico_board[(7, 2)] = [dico_board[(7, 4)][0], dico_board[(7, 4)][1], dico_board[(7, 4)][2], []]
                dico_board[(7, 4)] = [None, None, 0, []]
                dico_board[(7, 3)] = [dico_board[(7, 0)][0], dico_board[(7, 0)][1], dico_board[(7, 0)][2], []]
                dico_board[(7, 0)] = [None, None, 0, []]
                rook_piece = dico_board[(7, 3)][0]
                rook_piece.tile = (7, 3)  # Update the rook's tile
                rook_piece.first_move = False  # The rook has moved

            elif new_tile == (0, 6):  # Right Castling
                # Update dico_board for the special stroke "Right Castling"
                dico_board[(0, 6)] = [dico_board[(0, 4)][0], dico_board[(0, 4)][1], dico_board[(0, 4)][2], []]
                dico_board[(0, 4)] = [None, None, 0, []]
                dico_board[(0, 5)] = [dico_board[(0, 7)][0], dico_board[(0, 7)][1], dico_board[(0, 7)][2], []]
                dico_board[(0, 7)] = [None, None, 0, []]
                rook_piece = dico_board[(0, 5)][0]
                rook_piece.tile = (0, 5)  # Update the rook's tile
                rook_piece.first_move = False  # The rook has moved

            elif new_tile == (0, 2):  # Left Castling
                # Update dico_board for the special stroke "Left Castling"
                dico_board[(0, 2)] = [dico_board[(0, 4)][0], dico_board[(0, 4)][1], dico_board[(0, 4)][2], []]
                dico_board[(0, 4)] = [None, None, 0, []]
                dico_board[(0, 3)] = [dico_board[(0, 0)][0], dico_board[(0, 0)][1], dico_board[(0, 0)][2], []]
                dico_board[(0, 0)] = [None, None, 0, []]
                rook_piece = dico_board[(0, 3)][0]
                rook_piece.tile = (0, 3)  # Update the rook's tile
                rook_piece.first_move = False  # The rook has moved

        self.remove_from_list_piece_eaten(new_tile)  # Remove the piece eaten from the list of pieces (if there is one)
        self.update_dico_board_basic_stroke(king_piece, current_tile, new_tile)

    def move_other_pieces(self, moved_piece, current_tile, new_tile):
        self.remove_from_list_piece_eaten(new_tile)  # Remove the piece eaten from the list of pieces (if there is one)
        self.update_dico_board_basic_stroke(moved_piece, current_tile, new_tile)

    def move_piece(self, piece, current_tile, new_tile):
        """Move the piece to the new tile and update all the necessary elements."""

        if isinstance(piece, type(Pawn((6, 0), 1, True))):
            self.move_pawn(piece, current_tile, new_tile)

        elif isinstance(piece, type(self.king_white)): # If the piece is the king
            self.move_king(piece, current_tile, new_tile)

        else: # If the piece is not a pawn or a king
            self.move_other_pieces(piece, current_tile, new_tile)

        # Update position of the moved piece on the board => piece.tile = new_tile
        piece.tile = new_tile

        # Update the first move of the piece
        if piece.first_move: # If the piece is on its first move
            piece.first_move = False # The pawn is not on its first move anymore

    def JustMovedPawn(self, piece):
        """Check if the pawn just moved => If yes, return True."""
        if isinstance(piece, type(Pawn((6, 0), 1, True))):
            if piece.just_moved:
                return True
        return False

    # IA

    def get_all_possible_moves(self):
        dico_all_possible_moves_on_board = {}
        for piece in self.dico_list_pieces[-1]:
            if dico_board[piece.tile][3] != []:
                for move in dico_board[piece.tile][3]:
                    dico_all_possible_moves_on_board[piece] = [move, piece.tile]
        return dico_all_possible_moves_on_board

    def generate_random_moves(self):
        all_moves = self.get_all_possible_moves()
        random_piece = random.choice(list(all_moves.keys()))
        random_move, current_tile = all_moves[random_piece][0], all_moves[random_piece][1]
        return random_piece, random_move, current_tile

    def EvalPoints(self):
        total_point_black = 0
        for piece in self.dico_list_pieces[-1]:
            total_point_black += self.dico_points_pieces_black[type(dico_board[piece.tile][0])][piece.tile[0]][piece.tile[1]]

        total_point_white = 0
        for piece in self.dico_list_pieces[1]:
            total_point_white += self.dico_points_pieces_white[type(dico_board[piece.tile][0])][piece.tile[0]][piece.tile[1]]

        return total_point_white - total_point_black

    def generate_big_dico(self):
        dico = {}
        dico_all_moves = self.get_all_possible_moves()
        for piece in self.dico_list_pieces[-1]:
            dico[piece] = []
            for move in dico_all_moves[piece]:
                dico[piece].append(move)
                # SIMULATION
                save_color_tile = dico_board[move][2]
                dico_board[move][2] = - 1
                dico_board[piece.tile][2] = 0
                point_board = self.EvalPoints()
                dico[piece].append(point_board)
                # Reset simulation
                dico_board[move][2] = save_color_tile
                dico_board[piece.tile][2] = piece.color
        return dico

    def move_IA(self):
        time.sleep(0.2)
        #dico = self.generate_big_dico() # Piece : [Move, points]
        #self.minimax(all_moves, 3, - math.inf, math.inf, True)


        random_piece, random_move, current_tile = self.generate_random_moves()
        self.move_piece(random_piece, current_tile, random_move)
        return random_piece

    def minimax(self, parent_position, depth, alpha, beta, maximizingPlayer):
        #if depth == 0 or game over in position:
            #return static evaluation of position

        if maximizingPlayer: # Simulate that the turn is to the White player
            maxEval = - math.inf
            for child in parent_position:
                #eval = minimax(child, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else: # Simulate that the turn is to the Black player (= IA player)
            minEval = + math.inf
            for child in parent_position:
                #eval = minimax(child, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval