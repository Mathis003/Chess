from Assets import dico_board, LIST_BLACK_PIECES, LIST_WHITE_PIECES
from Configs import *

class Pieces:

    def __init__(self, screen, board, rect, tile, opponent_color, first_move=0):
        self.screen = screen
        self.board = board
        self.rect = rect # Rectangle of the piece
        self.tile = tile # The tile of the piece
        self.opponent_color = opponent_color # - 1 for white, 1 for black
        self.first_move = first_move

    def get_key(self, dico_board, val):
        for key, value in dico_board.items():
            if val == value[0]:
                return key

    def possible_moves(self):
        for piece in LIST_BLACK_PIECES:
            key = self.get_key(dico_board, piece)
            list_new_moves_possible = piece.update_possible_moves()
            for move in list_new_moves_possible:
                if move not in dico_board[key][3]:
                    dico_board[key][3].append(move)

        for piece in LIST_WHITE_PIECES:
            key = self.get_key(dico_board, piece)
            list_new_moves_possible = piece.update_possible_moves()
            for move in list_new_moves_possible:
                if move not in dico_board[key][3]:
                    dico_board[key][3].append(move)


    def move_piece(self, piece, current_tile, new_tile):
        # Remove the object (in the pieces list) from the old tile
        if dico_board[new_tile][0] != None:
            if dico_board[new_tile][2] == 1:
                LIST_WHITE_PIECES.remove(dico_board[new_tile][0])
            else:
                LIST_BLACK_PIECES.remove(dico_board[new_tile][0])
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

        # Update position of the piece on the board => piece.tile = new_tile
        piece.tile = new_tile

        try: # If the piece is a pawn
            if piece.first_move == True: # If the pawn is on its first move
                piece.first_move = False # The pawn is not on its first move anymore
        except:
            pass # If the piece is not a pawn