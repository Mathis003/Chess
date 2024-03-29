class Piece:
    
    def get_board_pieces(self):
        from src.variables import board_pieces
        return board_pieces

    def get_list_black_pieces(self):
        from src.variables import list_black_pieces
        return list_black_pieces

    def get_list_white_pieces(self):
        from src.variables import list_white_pieces
        return list_white_pieces

    def get_image(self, color_piece, list_image):
        if color_piece == 1:
            return list_image[0]
        else:
            return list_image[1]

    def switch_image(self, current_idx):
        self.image = self.images[1 - current_idx]
    
    def get_mod_move(self, new_tile):
        if self.get_board_pieces()[new_tile[0]][new_tile[1]] != None:
            return "capture"
        else:
            return "move"

    def add_piece(self, piece):
        if piece.color == 1:
            self.get_list_white_pieces().append(piece)
        elif piece.color == -1:
            self.get_list_black_pieces().append(piece)

    def remove_piece(self, piece):
        if piece != None:
            if piece.color == 1:
                self.get_list_white_pieces().remove(piece)
            else:
                self.get_list_black_pieces().remove(piece)
    
    def move_piece(self, current_tile, new_tile, idx_image):
        board_pieces = self.get_board_pieces()

        mod_of_move = self.get_mod_move(new_tile)
        piece_eaten = board_pieces[new_tile[0]][new_tile[1]]
        self.remove_piece(piece_eaten)

        board_pieces[new_tile[0]][new_tile[1]] = self
        board_pieces[current_tile[0]][current_tile[1]] = None
        self.tile = new_tile

        if self.first_move:
            self.first_move = False
        return mod_of_move
    
    def get_list_pieces(self, color_piece):
        if color_piece == 1:
            return self.get_list_white_pieces()
        else:
            return self.get_list_black_pieces()
    
    def get_king(self, color):
        for piece in self.get_list_pieces(color):
            try:
                # Test if rook_left is an argument of piece
                if piece.rook_left == None:
                    pass
                return piece
            except:
                pass
        return None

    def get_piece_that_check(self, moved_piece_color):
        for piece in self.get_list_pieces(moved_piece_color):
            piece.update_possible_moves()
            if self.get_king(-moved_piece_color).tile in piece.available_moves:
                return piece
        return None

    def removes_moves_that_doesnt_protect_king(self, moved_piece, opponent_piece, piece_that_check):
        board_pieces = self.get_board_pieces()

        opponent_king = self.get_king(-moved_piece.color)
        list_moves_to_remove = []

        # Begin Simulation 1
        board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = None
        self.remove_piece(piece_that_check)

        if self.king_in_chess(opponent_king):
            opponent_piece.available_moves = []
        else:
            for opponent_move in opponent_piece.available_moves:

                if opponent_move != piece_that_check.tile:
                
                    # Begin Simulation 2
                    save_piece_moved_tile = board_pieces[opponent_move[0]][opponent_move[1]]
                    board_pieces[opponent_move[0]][opponent_move[1]] = opponent_piece

                    piece_that_check.update_possible_moves()
                    if opponent_king.tile in piece_that_check.available_moves:
                        list_moves_to_remove.append(opponent_move)
                    
                    # End Simulation 2
                    board_pieces[opponent_move[0]][opponent_move[1]] = save_piece_moved_tile

            # End Simulation 1
            board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = opponent_piece

            for move_to_remove in list_moves_to_remove:
                opponent_piece.available_moves.remove(move_to_remove)

        self.add_piece(piece_that_check)

    def player_cant_move(self, piece_color):
        for piece in self.get_list_pieces(piece_color):
            if piece.available_moves != []:
                return False
        return True

    def remove_moves_that_puts_king_in_chess(self, moved_piece_color):
        board_pieces = self.get_board_pieces()
        opponent_king = self.get_king(-moved_piece_color)

        for opponent_piece in self.get_list_pieces(-moved_piece_color):
            list_moves_to_remove = []
            for piece in self.get_list_pieces(moved_piece_color):
                
                piece.update_possible_moves()
                if opponent_piece.tile in piece.available_moves:

                    # Begin Simulation 1
                    board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = None
                    for move_opponent_piece in opponent_piece.available_moves:

                        # Begin Simulation 2
                        save_piece_moved_tile = board_pieces[move_opponent_piece[0]][move_opponent_piece[1]]
                        board_pieces[move_opponent_piece[0]][move_opponent_piece[1]] = opponent_piece

                        piece.update_possible_moves()
                        if opponent_king.tile in piece.available_moves:
                            list_moves_to_remove.append(move_opponent_piece)
                        
                        # End Simulation 2
                        board_pieces[move_opponent_piece[0]][move_opponent_piece[1]] = save_piece_moved_tile

                    # End Simulation 1
                    board_pieces[opponent_piece.tile[0]][opponent_piece.tile[1]] = opponent_piece

            for move_to_remove in list_moves_to_remove:
                opponent_piece.available_moves.remove(move_to_remove) 
    
    def remove_moves_of_king_that_chess_him(self, opponent_king):
        board_pieces = self.get_board_pieces()
        list_moves_to_remove = []

        # Begin Simulation 1
        board_pieces[opponent_king.tile[0]][opponent_king.tile[1]] = None
        save_opponent_king_tile = opponent_king.tile
        for move_opponent_king in opponent_king.available_moves:
            
            # Begin Simulation 2
            save_opponent_king_moved_tile = board_pieces[move_opponent_king[0]][move_opponent_king[1]]
            board_pieces[move_opponent_king[0]][move_opponent_king[1]] = opponent_king
            opponent_king.tile = move_opponent_king

            if self.king_in_chess(opponent_king):
                list_moves_to_remove.append(move_opponent_king)

            # End Simulation 2
            board_pieces[move_opponent_king[0]][move_opponent_king[1]] =  save_opponent_king_moved_tile

        # End Simulation 1
        opponent_king.tile = save_opponent_king_tile
        board_pieces[opponent_king.tile[0]][opponent_king.tile[1]] = opponent_king

        for move_to_remove in list_moves_to_remove:
            opponent_king.available_moves.remove(move_to_remove)
    
    def king_in_chess(self, king):
        for piece in self.get_list_pieces(-king.color):
            piece.update_possible_moves()
            if king.tile in piece.available_moves:
                return True
        return False

    def update_available_moves(self, moved_piece):

        # Update all the available moves ignorings moves that put king in chess,...
        for piece in self.get_list_pieces(-moved_piece.color):
            piece.update_possible_moves()
        
        opponent_king = self.get_king(-moved_piece.color)
        # If the opponent king is not in chess
        if not self.king_in_chess(opponent_king):
            self.remove_moves_that_puts_king_in_chess(moved_piece.color)
            self.remove_moves_of_king_that_chess_him(opponent_king)

            if self.player_cant_move(-moved_piece.color):
                mod_of_move = "stalemate"
            else:
                mod_of_move = self.get_mod_move(moved_piece.tile)

        # If the opponent king is in chess
        else:
            mod_of_move = "check"
            for opponent_piece in self.get_list_pieces(-moved_piece.color):
                # If the piece is the king himself
                if opponent_piece == self.get_king(-moved_piece.color):
                    self.remove_moves_of_king_that_chess_him(opponent_piece)
                # If the piece is not the king
                else:
                    piece_that_check = self.get_piece_that_check(moved_piece.color)
                    self.removes_moves_that_doesnt_protect_king(moved_piece, opponent_piece, piece_that_check)
                
                if self.player_cant_move(-moved_piece.color):
                    mod_of_move = "checkmate"

        return mod_of_move