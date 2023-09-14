from src.all_pieces import Bishop, King

class Pieces:

    def __init__(self, board, king_white, king_black):
        self.board = board
        self.king_white = king_white
        self.king_black = king_black
    
    def get_list_pieces(self, color_piece):
        if color_piece == 1:
            return self.board.list_white_pieces
        else:
            return self.board.list_black_pieces
    
    def get_king(self, color):
        for piece in self.get_list_pieces(color):
            if type(piece) == type(King(None, [], [], None, None, [], [None, None], 0, True, None, None)):
                return piece
        return None
    
    def opponent_check(self, moved_piece):

        opponent_king = self.get_king(-moved_piece.color)
        for piece in self.get_list_pieces(moved_piece.color):
            if (opponent_king.tile in piece.available_moves):
                return True
        return False
    
    def stalemate(self, moved_piece):
        """
        Already check that the opponent king is not in chess!
        """
        opponent_king = self.get_king(-moved_piece.color)
        for opponent_piece in self.get_list_pieces(opponent_king.color):
            if opponent_piece.available_moves != []:
                return False
        return True

    def checkmate(self):
        """
        Already check that the opponent king is in chess!
        """
    
    def defend_checked_king(self, color_to_defend):

        can_defend = False
        king = self.get_king(color_to_defend)
        for piece in self.get_list_pieces(color_to_defend):
            if type(piece) != type(king):
                for opponent_piece in self.get_list_pieces(-color_to_defend):
                    for move_piece in piece.available_moves:
                        if move_piece not in opponent_piece.available_moves:
                            piece.available_moves.remove(move_piece)
                        else:
                            # Begin Simulation 1
                            self.board.board_pieces[piece.tile[0]][piece.tile[1]] = None
                            save_piece_moved_tile = self.board.board_pieces[move_piece[0]][move_piece[1]]
                            self.board.board_pieces[move_piece[0]][move_piece[1]] = piece

                            opponent_piece.update_possible_moves()
                            if king.tile in opponent_piece.available_moves:
                                piece.available_moves.remove(move_piece)
                            else:
                                can_defend = True
                            
                            # End Simulation 1
                            self.board.board_pieces[move_piece[0]][move_piece[1]] =  save_piece_moved_tile
        return can_defend

    

    def remove_moves_of_king_that_chess_him(self, moved_piece_color):

        # Begin Simulation 1
        king = self.get_king(moved_piece_color)
        opponent_king = self.get_king(-moved_piece_color)

        self.board.board_pieces[opponent_king.tile[0]][opponent_king.tile[1]] = None

        for piece in self.get_list_pieces(moved_piece_color):
            for move_opponent_king in opponent_king.available_moves:
                
                # Begin Simulation 2
                save_opponent_king_moved_tile = self.board.board_pieces[move_opponent_king.tile[0]][move_opponent_king.tile[1]]
                self.board.board_pieces[move_opponent_king.tile[0]][move_opponent_king.tile[1]] = opponent_king

                king.update_possible_moves()
                if opponent_king in piece.available_moves:
                    king.available_moves.remove(opponent_king)
                
                # End Simulation 2
                self.board.board_pieces[move_opponent_king.tile[0]][move_opponent_king.tile[1]] =  save_opponent_king_moved_tile

        # End Simulation 1
        self.board.board_pieces[king.tile[0]][king.tile[1]] = opponent_king
    

    def king_in_chess(self, moved_piece):

        opponent_king = self.get_king(-moved_piece.color)
        for piece in self.get_list_pieces(moved_piece.color):
            if opponent_king.tile in piece.available_moves:
                return True
        return False

    def removes_moves_that_doesnt_protect_king(self, moved_piece):
        for opponent_piece in self.get_list_pieces(-moved_piece.color):
            for move_piece in piece.available_moves:
                if move_piece not in opponent_piece.available_moves:
                    piece = None
                    piece.available_moves.remove(move_piece)
                else:
                    # Begin Simulation 1
                    self.board.board_pieces[piece.tile[0]][piece.tile[1]] = None
                    save_piece_moved_tile = self.board.board_pieces[move_piece[0]][move_piece[1]]
                    self.board.board_pieces[move_piece[0]][move_piece[1]] = piece

                    opponent_piece.update_possible_moves()
                    king = None
                    if king.tile in opponent_piece.available_moves:
                        piece.available_moves.remove(move_piece)
                    
                    # End Simulation 1
                    self.board.board_pieces[move_piece[0]][move_piece[1]] =  save_piece_moved_tile


    def update_available_moves(self, moved_piece):

        # Update all the available moves ignorings moves that put king in chess,...
        if moved_piece.color == 1:
            list_pieces = self.board.list_black_pieces
        else:
            list_pieces = self.board.list_white_pieces

        for piece in list_pieces:
            piece.update_possible_moves()
            print(piece.available_moves)
        print("====")

        # If the opponent king is not in chess
        if not self.king_in_chess(moved_piece):
            self.remove_moves_that_puts_king_in_chess(moved_piece.color)

        # If the opponent king is in chess
        else:
            king = self.get_king(moved_piece.color)
            for opponent_piece in self.get_list_pieces(-moved_piece.color):

                # If the piece is the king himself
                if opponent_piece == king:
                    self.remove_moves_of_king_that_chess_him(moved_piece.color)

                # If the piece is not the king
                else:
                    self.removes_moves_that_doesnt_protect_king(moved_piece)
        


    def remove_moves_that_puts_king_in_chess(self, moved_piece_color):

        king = self.get_king(-moved_piece_color)

        for piece in self.get_list_pieces(moved_piece_color):
            for opponent_piece in self.get_list_pieces(-moved_piece_color):
                
                if opponent_piece.tile in piece.available_moves:

                    # Begin Simulation 1
                    self.board.board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = None

                    for move_opponent_piece in opponent_piece.available_moves:

                        # Begin Simulation 2
                        save_piece_moved_tile = self.board.board_pieces[move_opponent_piece[0]][move_opponent_piece[1]]
                        self.board.board_pieces[move_opponent_piece[0]][move_opponent_piece[1]] = opponent_piece
                        piece.update_possible_moves()
                        if king.tile in piece.available_moves:
                            opponent_piece.available_moves.remove(move_opponent_piece)
                        
                        # End Simulation 2
                        self.board.board_pieces[move_opponent_piece[0]][move_opponent_piece[1]] = save_piece_moved_tile

                    # End Simulation 1
                    self.board.board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = opponent_piece