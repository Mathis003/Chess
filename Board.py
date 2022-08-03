from Assets import dico_board
import pygame
from Configs import *

class Board:
    """ Represent the board on the screen"""
    def __init__(self, screen):
        self.screen = screen

    def get_key(self, dico_board, val):
        for key, value in dico_board.items():
            if val == value[0]:
                return key

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
        for i in range(ROW):
            for j in range(COL):
                if dico_board[(i, j)][2] != 0 and dico_board[(i, j)][1] != None: # If the tile is not empty
                    self.screen.blit(dico_board[(i, j)][1], (j * SQUARE, i * SQUARE))

    def draw_possible_moves(self, tile_piece):
        """ Draw the possible moves of a piece """
        for move_tile in dico_board[tile_piece][3]:
            pygame.draw.circle(self.screen, GREEN, ((move_tile[1] + 1/2) * SQUARE, (move_tile[0] + 1/2) * SQUARE), SQUARE / 8)