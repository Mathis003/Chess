from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES, pygame
from Configs import *

class Board:
    """ Represent the board on the screen"""
    def __init__(self, screen):
        self.screen = screen

    def draw_tile_on_board(self, i, j, light_color, dark_color):
        if i % 2 == 0:  # If i is even
            if j % 2 == 0:  # If j is even
                pygame.draw.rect(self.screen, light_color, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
            else:  # If j is odd
                pygame.draw.rect(self.screen, dark_color, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
        else:  # If i is odd
            if j % 2 == 0:  # If j is even
                pygame.draw.rect(self.screen, dark_color, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
            else:  # If j is odd
                pygame.draw.rect(self.screen, light_color, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))

    def draw_board(self):
        """ Draw the board's squares """
        for i in range(ROW):
            for j in range(COL):
                self.draw_tile_on_board(i, j, LIGHT_COLOR, DARK_COLOR)

    def draw_pieces(self):
        """ Draw the pieces on the board"""
        for piece in LIST_BLACK_PIECES: # Loop for each black piece
            if dico_pieces[piece][1] != None:
                self.screen.blit(dico_pieces[piece][1], (dico_pieces[piece][0][1] * SQUARE, dico_pieces[piece][0][0] * SQUARE))
        for piece in LIST_WHITE_PIECES: # Loop for each white piece
            if dico_pieces[piece][1] != None:
                self.screen.blit(dico_pieces[piece][1], (dico_pieces[piece][0][1] * SQUARE, dico_pieces[piece][0][0] * SQUARE))

    def draw_possible_moves(self, tile_piece):
        """ Draw the new color of the square of all possible moves of a piece"""
        try:
            for move_tile in dico_board[tile_piece][3]: # Loop for each possible move
                self.draw_tile_on_board(move_tile[0], move_tile[1], COLOR_POSSIBLE_MOVES_LIGHT, COLOR_POSSIBLE_MOVES_DARK)
        except KeyError:
            pass # Deal with the error of the piece not being on the board ( at the beginning of the game, initialize on purpose the tile on (-1, -1))

    def draw_tile_player(self, tile_player, color):
        """ Draw the new color of the square of the player's tile"""
        pygame.draw.rect(self.screen, color, (tile_player[1] * SQUARE, tile_player[0] * SQUARE, SQUARE, SQUARE))