import time

from Pieces import Pieces
from Board import Board
from Assets import screen, dico_board, dico_pieces, pygame, king_white, king_black
from Configs import *


# Initialize classes
board = Board(screen)
pieces = Pieces(king_white, king_black)
pygame.init()

class Game:

    def __init__(self, screen, board, pieces):
        # All classes
        self.screen = screen
        self.board = board
        self.pieces = pieces

        # All variables
        self.running = True
        self.ChessMod = False
        self.dico_mouse = {"click_before_playing" : False, "click_after_playing" : False}
        self.dico_turn = {"turn_white" : True, "turn_black" : False}
        self.mouse_pressed = False
        self.player_tile_clicked = (-1, -1)
        self.player_tile_moved = (-1, -1)
        self.enter = False
        self.end_pressed = False
        self.enter_mouse_pressed = False
        self.list_color_case = [(-1, -1), (-1, -1)]
        self.color_case_waiting = (-1, -1)

    def run(self):
        pos_mouse = [0, 0]
        enter = True
        while self.running: # Main loop

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user clicks the close button
                    self.running = False # Stop the game
                    pygame.quit() # Close the game
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN: # If the mouse is clicked
                    initial_pos_mouse = pygame.mouse.get_pos()  # Get the initial mouse position of the click (x, y)
                    tile_clicked = (initial_pos_mouse[1] // SQUARE, initial_pos_mouse[0] // SQUARE)  # Tile clicked
                    if dico_board[tile_clicked][0] != None: # If the tile clicked isn't empty
                        self.enter = True
                        self.player_tile_clicked = tile_clicked # Update the player_tile_clicked

                        self.list_color_case[0] = tile_clicked

                        save_image_tile_clicked = dico_board[self.player_tile_clicked][1] # Save the image of the tile clicked
                        self.enter_mouse_pressed = True
                        dico_pieces[dico_board[self.player_tile_clicked][0]][1] = None # Update the image of the piece and replace it by None


            self.mouse_pressed = pygame.mouse.get_pressed()[0]
            self.board.draw_board()
            # Display the colors of the possible moves / the tile clicked
            self.board.draw_tile_player(self.list_color_case[0], COLOR_PLAYER_BEFORE_MOVE)  # Draw the tile clicked by the player
            self.board.draw_tile_player(self.list_color_case[1], COLOR_PLAYER_AFTER_MOVE)  # Draw the tile played by the player
            self.board.draw_tile_player(self.color_case_waiting, COLOR_PLAYER_BEFORE_MOVE)  # Draw the tile played by the player
            self.board.draw_possible_moves(self.player_tile_clicked)
            self.board.draw_pieces()


            if self.mouse_pressed and self.enter_mouse_pressed: # If the mouse is pressed
                if self.player_tile_clicked != (-1, -1): # If the player_tile_clicked isn't (-1, -1)
                    pos_mouse = pygame.mouse.get_pos() # Get the current mouse position (x, y)
                    self.board.draw_tile_player(self.player_tile_clicked, COLOR_PLAYER_BEFORE_MOVE) # Draw the tile clicked by the player
                    # Update the image of the piece clicked
                    dico_board[self.player_tile_clicked][0].rect.center = pos_mouse
                    self.screen.blit(save_image_tile_clicked, dico_board[self.player_tile_clicked][0].rect)

            if not self.mouse_pressed and self.enter: # If the mouse is not pressed anymore
                self.enter_mouse_pressed = False
                #dico_board[self.player_tile_clicked][1] = save_image_tile_clicked
                self.enter = False
                self.end_pressed = True

            if self.end_pressed: # If the player clicked to play (if the player stayed the left button mouse pressed => This section is useless
                self.end_pressed = False
                final_pos_mouse = pygame.mouse.get_pos() # Get the final mouse position of the click (x, y)
                self.player_tile_moved = (final_pos_mouse[1] // SQUARE, final_pos_mouse[0] // SQUARE) # Tile moved
                if list(self.player_tile_moved) in dico_board[self.player_tile_clicked][3]:
                    piece_moved = dico_board[self.player_tile_moved][0]
                    if self.pieces.Promotion_Pawn(dico_board[self.player_tile_clicked][0], self.player_tile_moved):
                        self.pieces.PromotePawn_into_Queen(dico_board[self.player_tile_clicked][0], self.player_tile_moved)

                    else:
                        if dico_board[self.player_tile_moved][2] in [0, - dico_board[self.player_tile_clicked][2]]:
                            self.pieces.move_piece(dico_board[self.player_tile_clicked][0], self.player_tile_clicked, self.player_tile_moved)
                            piece_moved = dico_board[self.player_tile_moved][0]
                            dico_pieces[piece_moved][1] = save_image_tile_clicked

                    self.list_color_case[1] = self.player_tile_moved
                    self.color_case_waiting = tile_clicked
                    self.pieces.possible_moves(piece_moved, self.player_tile_clicked, self.player_tile_moved)  # Update the movement of the pieces on which there are changes about their possibilities of moves

                    if self.pieces.CheckChess(piece_moved):  # If the piece put the opponent king in check
                        self.pieces.ChessMod_update_possibles_move(piece_moved)  # Reupdate correctly the possibility of the pieces to move and protect the king
                        if self.pieces.Check_Checkmate(piece_moved):  # If the king is in checkmate
                            print("END GAME")  # End the game

                else:
                    piece_moved = dico_board[self.player_tile_clicked][0]
                    dico_pieces[piece_moved][1] = save_image_tile_clicked
                    # Reset the color of the tile clicked
                    self.player_tile_clicked = (-1, -1)
                    self.list_color_case[0] = (-1, -1)



            if self.dico_turn["turn_white"]: # If the turn is to the white
                pass

            if self.dico_turn["turn_black"]: # If the turn is to the black
                pass

            pygame.display.update()




if __name__ == '__main__': # If the program is run directly, not imported
    game = Game(screen, board, pieces) # Create a new game
    game.run() # Run the game