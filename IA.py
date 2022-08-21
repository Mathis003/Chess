from Assets import dico_board
import time
import math
import random

# INUTILE POUR LE MOMENT => CLASSE NON APPELE
# PLEINS DE BUGS , TOUT REFAIRE => J'AI LAISSER POUR AVOIR UN SQUELETTE SI NECESSAIRE

class IA_Player:

    def __init__(self):
        self.move_piece = None
        self.dico_list_pieces = None
        self.dico_points_pieces_black = None
        self.dico_points_pieces_white = None

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
        time.sleep(0.7)
        #dico = self.generate_big_dico() # Piece : [Move, points]
        #self.minimax(all_moves, 3, - math.inf, math.inf, True)
        random_piece, random_move, current_tile = self.generate_random_moves()
        mod_of_move = self.move_piece(random_piece, current_tile, random_move)
        return random_piece, current_tile, random_move, mod_of_move

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