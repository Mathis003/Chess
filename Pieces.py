from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES

class Pieces:

    def __init__(self):
        pass

    def get_key(self, val):
        """ Search the key who match with the value 'val' in dico_board """
        for key, value in dico_board.items():
            if val == value[0]:
                return key

    def possible_moves(self):
        for piece in LIST_BLACK_PIECES: # Loop for each black piece
            key = self.get_key(piece) # find the right key
            list_new_moves_possible = piece.update_possible_moves() # Update possible moves of the piece
            # Move is in fact a tile which the piece can move on
            for move in list_new_moves_possible: # Loop for each move
                if move not in dico_board[key][3]: # If the move isn't in the list
                    dico_board[key][3].append(move) # Add the move to the list

        for piece in LIST_WHITE_PIECES: # Loop for each white piece
            key = self.get_key(piece) # find the right key
            list_new_moves_possible = piece.update_possible_moves() # Update possible moves of the piece
            # Move is in fact a tile which the piece can move on
            for move in list_new_moves_possible: # Loop for each move
                if move not in dico_board[key][3]: # If the move isn't in the list
                    dico_board[key][3].append(move) # Add the move to the list


    def move_piece(self, piece, current_tile, new_tile):
        # Remove the object (in the pieces list) from the old tile
        if dico_board[new_tile][0] != None:
            if dico_board[new_tile][2] == 1:
                LIST_WHITE_PIECES.remove(dico_board[new_tile][0])
            else:
                LIST_BLACK_PIECES.remove(dico_board[new_tile][0])
        print(new_tile)
        # Update the position of the piece_image on the board (which tile)
        dico_pieces[piece][0] = new_tile

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