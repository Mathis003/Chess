from Pieces import Pieces
from Board import Board
from Assets import screen, dico_board, pygame
from Configs import *
import time

# Initialize classes
board = Board(screen)
pieces = Pieces()

pygame.init()

class Game:

    def __init__(self, screen, board, pieces):
        # All classes
        self.screen = screen
        self.board = board
        self.pieces = pieces

        # All variables
        self.running = True
        self.dico_mouse = {"click_before_playing" : False, "click_after_playing" : False}

    def run(self):
        tile = None
        pos_mouse = [0, 0]
        save_tile = True
        while self.running: # Main loop

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user clicks the close button
                    self.running = False # Stop the game
                    pygame.quit() # Close the game
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN: # If the mouse is clicked
                    pos_mouse = pygame.mouse.get_pos()  # Get the mouse position (x, y)
                    # Update the dico_mouse correctly
                    if self.dico_mouse["click_before_playing"] == False:
                        tile = (pos_mouse[1] // SQUARE, pos_mouse[0] // SQUARE)
                        if dico_board[tile][3] != []:  # If the pressed piece can move
                            start = time.time()
                            self.dico_mouse["click_before_playing"] = True
                            self.dico_mouse["click_after_playing"] = False
                    else:
                        self.dico_mouse["click_before_playing"] = False
                        self.dico_mouse["click_after_playing"] = True

            self.board.draw_board()
            self.board.draw_pieces()
            self.pieces.possible_moves()


            # Deal with mouse's clicks and update pieces's positions,...
            if self.dico_mouse["click_before_playing"]:  # If the player clicked to play
                if pygame.mouse.get_pressed()[0] and time.time() - start >= 0.12: # If the left mouse button is clicked
                    if save_tile:
                        tile = (pos_mouse[1] // SQUARE, pos_mouse[0] // SQUARE)
                        save_tile = False
                        save_image = dico_board[tile][1]

                    dico_board[tile][1] = None # Remove the image's pieces from the board during the move (to avoid the piece to be drawn twice)
                    pos_mouse = pygame.mouse.get_pos()
                    dico_board[tile][0].rect.center = pos_mouse
                    self.screen.blit(save_image, dico_board[tile][0].rect)
                    pygame.display.update()

                elif not pygame.mouse.get_pressed()[0]: # If the left mouse button is released
                    if save_tile:
                        tile = (pos_mouse[1] // SQUARE, pos_mouse[0] // SQUARE)
                        save_image = dico_board[tile][1]

                    dico_board[tile][1] = save_image # Put the image's pieces back on the board
                    self.dico_mouse["click_before_playing"] = False
                    self.dico_mouse["click_after_playing"] = True
                    save_tile = True


                self.board.draw_possible_moves(tile)
                pygame.display.update()


            if self.dico_mouse["click_after_playing"]: # If the player clicked to play (if the player stayed the left button mouse pressed => This section is useless
                save_tile = True
                if [pos_mouse[1] // SQUARE, pos_mouse[0] // SQUARE] in dico_board[tile][3]:  # If the player clicked to play
                    new_tile = (pos_mouse[1] // SQUARE, pos_mouse[0] // SQUARE)
                    if dico_board[new_tile][2] in [0, - dico_board[tile][2]]:
                        self.pieces.move_piece(dico_board[tile][0], tile, new_tile)
                    self.dico_mouse["click_after_playing"] = False
            pygame.display.update()


if __name__ == '__main__': # If the program is run directly, not imported
    game = Game(screen, board, pieces) # Create a new game
    game.run() # Run the game