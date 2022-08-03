from Assets import dico_board, dico_pieces, LIST_BLACK_PIECES, LIST_WHITE_PIECES, pygame
from Configs import *

class Board:
    """ Represent the board on the screen"""
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self):
        """ Draw the board's squares """
        for i in range(ROW):
            for j in range(COL):
                if i % 2 == 0: # If i is even
                    if j % 2 == 0: # If j is even
                        pygame.draw.rect(self.screen, WHITE, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
                    else: # If j is odd
                        pygame.draw.rect(self.screen, RED_DARK, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
                else: # If i is odd
                    if j % 2 == 0: # If j is even
                        pygame.draw.rect(self.screen, RED_DARK, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))
                    else: # If j is odd
                        pygame.draw.rect(self.screen, WHITE, (j * SQUARE, i * SQUARE, SQUARE, SQUARE))

    def draw_pieces(self):
        """ Draw the pieces on the board"""
        for piece in LIST_BLACK_PIECES: # Loop for each black piece
            self.screen.blit(dico_pieces[piece][1], (dico_pieces[piece][0][1] * SQUARE, dico_pieces[piece][0][0] * SQUARE))
        for piece in LIST_WHITE_PIECES: # Loop for each white piece
            self.screen.blit(dico_pieces[piece][1], (dico_pieces[piece][0][1] * SQUARE, dico_pieces[piece][0][0] * SQUARE))

    def draw_possible_moves(self, tile_piece):
        """ Draw the possible moves of a piece """
        for move_tile in dico_board[tile_piece][3]: # Loop for each possible move
            pygame.draw.circle(self.screen, GREEN, ((move_tile[1] + 1/2) * SQUARE, (move_tile[0] + 1/2) * SQUARE), SQUARE / 8)