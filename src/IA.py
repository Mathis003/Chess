from src.all_pieces import *
import numpy as np


### Create matrix of pieces's points in function of their position on the board ###

matrix_points_pawn_white = [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

matrix_points_pawn_black = list(np.array(matrix_points_pawn_white)[::-1]) # Reverse the matrix

matrix_points_knight_white = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]
matrix_points_knight_black = matrix_points_knight_white

matrix_points_bishop_white = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

matrix_points_bishop_black = list(np.array(matrix_points_bishop_white)[::-1]) # Reverse the matrix

matrix_points_rook_white = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

matrix_points_rook_black = list(np.array(matrix_points_rook_white)[::-1]) # Reverse the matrix

matrix_points_queen_white = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

matrix_points_queen_black = matrix_points_queen_white

matrix_points_king_white = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

matrix_points_king_black = list(np.array(matrix_points_king_white)[::-1]) # Reverse the matrix

dico_points_pieces_white = {type(Pawn((7, 4), 1)): matrix_points_pawn_white,
                            type(Queen((7, 4), 1)): matrix_points_queen_white,
                            type(King((7, 4), 1, None, None)): matrix_points_king_white,
                            type(Bishop((7, 4), 1)): matrix_points_bishop_white,
                            type(Knight((7, 4), 1)): matrix_points_knight_white,
                            type(Rook((7, 4), 1)): matrix_points_rook_white}

dico_points_pieces_black = {type(Pawn((7, 4), 1)): matrix_points_pawn_black,
                            type(Queen((7, 4), 1)): matrix_points_queen_black,
                            type(King((7, 4), 1, None, None)): matrix_points_king_black,
                            type(Bishop((7, 4), 1)): matrix_points_bishop_black,
                            type(Knight((7, 4), 1)): matrix_points_knight_black,
                            type(Rook((7, 4), 1)): matrix_points_rook_black}

class IA_Player:

    def __init__(self, piece):
        self.piece = piece

    def get_list_pieces(self, piece_color):
        from src.variables import list_white_pieces
        from src.variables import list_black_pieces

        if piece_color == 1:
            return list_white_pieces
        else:
            return list_black_pieces

    def get_dico_score(self, piece):
        if piece.color == 1:
            return dico_points_pieces_white
        else:
            return dico_points_pieces_black

    def evaluate_position_piece(self, piece):
        dico_score = self.get_dico_score(piece)
        if piece == None:
            return 0
        return dico_score[type(piece)]

    def evaluate_board(self, board):
        score = 0
        for i in range(0, ROW):
            for j in range(0, COL):
                score += self.evaluate_position_piece(board[i][j])
        return score
    
    def create_tree(self, piece_moved, depth):
        from src.variables import board_pieces

        save_board_pieces = board_pieces
        root_node = Node(board_pieces, None, True)
        self.create_children(depth, root_node, piece_moved)
        board_pieces = save_board_pieces
        return root_node
    
    def create_children(self, depth, root_node, piece_moved):

        from src.variables import board_pieces
        from src.variables import list_white_pieces
        from src.variables import list_black_pieces

        if depth != 0:
            for piece in self.get_list_pieces(-piece_moved.color):
                for move in piece.available_moves:

                    save_board_pieces = board_pieces
                    save_list_white_pieces = list_white_pieces
                    save_list_black_pieces = list_black_pieces

                    piece.move_piece(piece.tile, move, 0)
                    self.piece.update_available_moves(piece_moved)

                    child = Node(board_pieces, move, not root_node.IA_player)
                    root_node.children.append(child)

                    self.create_children(depth - 1, child, piece)

                    board_pieces = save_board_pieces
                    list_white_pieces = save_list_white_pieces
                    list_black_pieces = save_list_black_pieces
    
    def minimax(self, root_node, depth, maximizing_player):

        # If we reach the maximum depth (base case)
        if depth == 0:
            if root_node.value == 0:
                root_node.value += self.evaluate_board(root_node.board)
            return root_node.value
        else:
            if root_node.children == []:
                return root_node.value

        # If it's the maximizing player
        if root_node.player != maximizing_player:
            max_eval = -np.inf
            for child in root_node.children:
                eval = self.minimax(child, depth - 1, maximizing_player)
                max_eval = max(max_eval, eval)
            root_node.value = max_eval # Update the value of the node
            return max_eval

        # If it's the minimizing player
        else:
            min_eval = np.inf
            for child in root_node.children:
                eval = self.minimax(child, depth - 1, maximizing_player)
                min_eval = min(min_eval, eval)
            root_node.value = min_eval # Update the value of the node
            return min_eval

    
    def IA_move(self, piece_moved, depth):

        # Créer l'arbre
        root_node = self.create_tree(piece_moved, depth)
        best_score = self.minimax(root_node, depth, True)

        list_best_child = []

        # Check which move(s) correspond to the best score
        for child in root_node.children:
            if child.value == best_score:
                list_best_child.append(child)

        # If there is only one move
        if len(list_best_child) == 1:
            best_move = list_best_child[0].move
        
        # If there are several moves
        else:
            pass

        return best_move


class Node:
    def __init__(self, root, move, IA_player):
        self.root = root
        self.IA_player = IA_player
        self.move = move
        self.value = 0
        self.children = []