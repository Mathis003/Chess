import sys
sys.path.append("/Users/mathisdelsart/PycharmProjects/Chess-Game Project/Chess-Game/Game/All_Configs")
import pygame
from Variables import LIST_BLACK_PIECES, LIST_WHITE_PIECES, dico_board
from Configs import *

class Board:
    """ Represent the board on the screen"""
    def __init__(self, screen):
        self.screen = screen

    def draw_tile(self, tile, mod_board, intensity):
        """
        Draw the rect of a tile with the good color
        :param tile: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number
        :param mod_board: the mod of the color board
        :param intensity: 'dark' or 'light' => always a contrast with tiles next each other
        """
        if mod_board == "brown_mod":
            if intensity == "dark":
                pygame.draw.rect(self.screen, COLOR_PLAYER_BEFORE_MOVE_BROWN, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))
            elif intensity == "light":
                pygame.draw.rect(self.screen, COLOR_PLAYER_AFTER_MOVE_BROWN, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))
        elif mod_board == "green_mod":
            if intensity == "dark":
                pygame.draw.rect(self.screen, COLOR_PLAYER_BEFORE_MOVE_GREEN, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))
            elif intensity == "light":
                pygame.draw.rect(self.screen, COLOR_PLAYER_AFTER_MOVE_GREEN, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))
        elif mod_board == "blue_mod":
            if intensity == "dark":
                pygame.draw.rect(self.screen, COLOR_PLAYER_BEFORE_MOVE_BLUE, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))
            elif intensity == "light":
                pygame.draw.rect(self.screen, COLOR_PLAYER_AFTER_MOVE_BLUE, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))

    def draw_tile_basic_board(self, tile, color):
        """
        Draw the rect of a tile with the good color
        :param tile: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number
        :param color: new color of the tile
        """
        pygame.draw.rect(self.screen, color, (tile[1] * SQUARE, tile[0] * SQUARE, SQUARE, SQUARE))

    def draw_tile_on_board(self, i, j, light_color, dark_color):
        """
        Draw the board's tile's new color (in function of the tile's position).
        :param i: tile's ROW number
        :param j: tile's COL number
        :param light_color: Color of light squares
        :param dark_color: Color of dark squares
        """
        if i % 2 == 0:  # If i is even
            if j % 2 == 0:  # If j is even
                self.draw_tile_basic_board((i, j), light_color)
            else:  # If j is odd
                self.draw_tile_basic_board((i, j), dark_color)
        else:  # If i is odd
            if j % 2 == 0:  # If j is even
                self.draw_tile_basic_board((i, j), dark_color)
            else:  # If j is odd
                self.draw_tile_basic_board((i, j), light_color)

    def draw_board(self, mod_board):
        """
        Draw all the board's tiles
        :param mod_board: mod of the board's color
        """
        if mod_board == "brown_mod":
            for i in range(ROW):
                for j in range(COL):
                    self.draw_tile_on_board(i, j, LIGHT_COLOR_BROWN, DARK_COLOR_BROWN)
        elif mod_board == "green_mod":
            for i in range(ROW):
                for j in range(COL):
                    self.draw_tile_on_board(i, j, LIGHT_COLOR_GREEN, DARK_COLOR_GREEN)
        elif mod_board == "blue_mod":
            for i in range(ROW):
                for j in range(COL):
                    self.draw_tile_on_board(i, j, LIGHT_COLOR_BLUE, DARK_COLOR_BLUE)

    def draw_pieces(self):
        """
        Draw all the pieces on the board.
        """
        for piece in LIST_BLACK_PIECES: # Loop for each black piece
            if dico_board[piece.tile][1] != None: # If the piece isn't pressed on the board => otherwise the image is None => = "Don't draw it"
                self.screen.blit(dico_board[piece.tile][1], (piece.tile[1] * SQUARE, piece.tile[0] * SQUARE))
        for piece in LIST_WHITE_PIECES: # Loop for each white piece
            if dico_board[piece.tile][1] != None: # If the piece isn't pressed on the board => otherwise the image is None => = "Don't draw it"
                self.screen.blit(dico_board[piece.tile][1], (piece.tile[1] * SQUARE, piece.tile[0] * SQUARE))

    def draw_possible_moves(self, tile_piece):
        """
        Draw the tile's new color of the pieces's all possible moves.
        :param tile_piece: tuple (a, b) where 'a' is the COL tile's number and 'b', the ROW tile's number (where the piece is)
        """
        if tile_piece != (-1, -1):
            for move_tile in dico_board[tile_piece][3]: # Loop for each possible move
                self.draw_tile_on_board(move_tile[0], move_tile[1], COLOR_POSSIBLE_MOVES_LIGHT, COLOR_POSSIBLE_MOVES_DARK)