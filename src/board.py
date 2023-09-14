import pygame
from src.configs import *

class Board:
    
    def __init__(self, screen):
        self.screen = screen
        
    def change_image(self):
        for piece in self.dico_list_pieces[1]:
            piece.current_idx_image = abs(1 - piece.current_idx_image)

    def draw_tile(self, tile, color):
        pygame.draw.rect(self.screen, color, (tile[1] * SIZE_SQUARE, tile[0] * SIZE_SQUARE, SIZE_SQUARE, SIZE_SQUARE))
    
    def check_dark_tile(self, tile):
        if tile[0] % 2 == 0:
            return (tile[1] % 2 != 0)
        else:
            return (tile[1] % 2 == 0)

    def draw_board(self, mod_board):
        for i in range(ROW):
            for j in range(COL):
                if self.check_dark_tile((i, j)):
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][1])
                else:
                    self.draw_tile((i, j), COLORS_BOARD[mod_board][0])
    
    def draw_possible_moves(self, available_moves):
        for move_tile in available_moves:
            if self.check_dark_tile(move_tile):
                self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_DARK)
            else:
                self.draw_tile(move_tile, COLOR_POSSIBLE_MOVES_LIGHT)
    
    def draw_pieces(self, list_pieces):
        for piece in list_pieces:
            if piece.image != None:
                self.screen.blit(piece.image, (piece.tile[1] * SIZE_SQUARE, piece.tile[0] * SIZE_SQUARE))