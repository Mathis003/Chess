from Assets import dico_board, pygame
from Configs import *

pygame.init() # Initialize the pygame module

class Game:
    """Game class represent the Game himself with the method Run() that launch the game."""

    def __init__(self, screen, board, pieces):
        # All classes
        self.screen = screen
        self.board = board
        self.pieces = pieces

        # All variables (configs)
        self.running = True  # Boolean to know if the game is running or not (True = running, False = not running)
        self.dico_turn = {"turn_white": True, "turn_black": False}  # Dictionary to know which player is playing
        self.player_tile_clicked = (-1,
                                    -1)  # Tile where the player clicked on the board to begin to play (initialize on (-1, -1) to be out of the board without causing error)
        self.player_tile_moved = (-1,
                                  -1)  # Tile where the player clicked on the board to move (after playing) (initialize on (-1, -1) to be out of the board without causing error)
        self.enter_mouse_pressed = False  # Allow to not click after drop the mouse's pression on a random tile and move the Rect on the image of the piece just before (If True = pressed mouse and Rect's moving, if False = no pressing mouse and Rect's not moving)
        self.list_color_case = [(-1, -1), (-1,
                                           -1)]  # List of the color of the case where the player clicked on the board (to have the historic and draw constantly the color until the next player play)
        self.color_case_waiting = (-1,
                                   -1)  # Color of the case where the player clicked on the board (to have the historic and draw constantly the color until the next player play)
        self.enter_to_reset_EnPassant = False  # Allow to reset some stuffs for the "En Passant" move
        self.save_pawn_first_move = None  # Save the object : Pawn that has done, the turn before, his first move => Will be reset the next Turn => Usefull for the "En Passant" rule :)
        self.save_image_tile_clicked = None  # Save the image of the tile clicked => Will be reset the next Turn
        self.mouse_pressed = False  # Boolean to know if the mouse is pressed or not (True = pressed, False = not pressed)
        self.piece_moved = None  # Save the object : Piece that has been moved => Will be reset the next Turn

    def update_necessary_variables(self, tile_clicked):
        """Update some necessary variables"""
        self.player_tile_clicked = tile_clicked  # Update the player_tile_clicked
        self.list_color_case[0] = tile_clicked
        self.save_image_tile_clicked = dico_board[self.player_tile_clicked][1]  # Save the image of the tile clicked
        self.enter_mouse_pressed = True
        dico_board[self.player_tile_clicked][1] = None  # Update the image of the piece and replace it by None

    def change_turn(self):
        """Change the player's turn"""
        if self.dico_turn["turn_white"]:
            self.dico_turn["turn_white"] = False
            self.dico_turn["turn_black"] = True
        else:
            self.dico_turn["turn_white"] = True
            self.dico_turn["turn_black"] = False

    def run(self):
        while self.running:  # Main loop

            # Events

            for event in pygame.event.get():  # Loop for each event
                if event.type == pygame.QUIT:  # If the user clicks the close button
                    self.running = False  # Stop the game
                    pygame.quit()  # Close the game
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # If the mouse is clicked
                    initial_pos_mouse = pygame.mouse.get_pos()  # Get the initial mouse position of first the click (x, y) to take a piece
                    tile_clicked = (initial_pos_mouse[1] // SQUARE, initial_pos_mouse[0] // SQUARE)  # Tile clicked

                    if self.dico_turn["turn_white"]:  # If the turn is for the white (white player)
                        if dico_board[tile_clicked][0] != None:  # If the tile clicked isn't empty
                            if dico_board[tile_clicked][0].color == 1:  # If the tile clicked is a white piece
                                self.update_necessary_variables(tile_clicked)  # Update the necessary variables

                    if self.dico_turn["turn_black"]:  # If the turn is for the black (black player)
                        if dico_board[tile_clicked][0] != None:  # If the tile clicked isn't empty
                            if dico_board[tile_clicked][0].color == -1:  # If the tile clicked is a white piece
                                self.update_necessary_variables(tile_clicked)  # Update the necessary variables

            # Update the elements of the game (board, pieces, ...)

            self.mouse_pressed = pygame.mouse.get_pressed()[0]  # Update the mouse_pressed variable
            # Draw all the tile on the board
            self.board.draw_board()
            # Display the colors of the possible moves / the tile clicked
            self.board.draw_tile(self.list_color_case[0],
                                 COLOR_PLAYER_BEFORE_MOVE)  # Draw the tile clicked by the player
            self.board.draw_tile(self.list_color_case[1], COLOR_PLAYER_AFTER_MOVE)  # Draw the tile played by the player
            self.board.draw_tile(self.color_case_waiting,
                                 COLOR_PLAYER_BEFORE_MOVE)  # Draw the tile played by the player
            self.board.draw_possible_moves(self.player_tile_clicked)
            # Display the pieces on the board (Done at the end of the loop to be sure that the pieces aren't hide by the tiles's color)
            self.board.draw_pieces()

            # Section use during one of the player plays and keep the mouse pressed to choose a tile to move

            if self.mouse_pressed and self.enter_mouse_pressed:  # If the mouse is pressed and the enter_mouse_pressed is open (= True)
                if self.player_tile_clicked != (
                -1, -1):  # If the player_tile_clicked isn't (-1, -1) => Different of the initialisation
                    pos_mouse = pygame.mouse.get_pos()  # Get the current mouse position (x, y) (usefull to update the rect's position of the piece)
                    self.screen.blit(self.save_image_tile_clicked,
                                     pygame.Rect(pos_mouse[0] - SQUARE / 2, pos_mouse[1] - SQUARE / 2, SQUARE,
                                                 SQUARE))  # Update the image of the piece clicked

            # Section use during one of the player has finished to play and release the mouse to choose a tile to move (until the player press the mouse again)

            if not self.mouse_pressed and self.enter_mouse_pressed:  # If the mouse is not pressed anymore and the enter_mouse_pressed is open (= True)
                self.enter_mouse_pressed = False  # Close the enter_mouse_pressed variable to pass this section just ONCE
                final_pos_mouse = pygame.mouse.get_pos()  # Get the final mouse position of the click (x, y)
                self.player_tile_moved = (final_pos_mouse[1] // SQUARE, final_pos_mouse[0] // SQUARE)  # Tile moved
                if self.player_tile_moved in dico_board[self.player_tile_clicked][
                    3]:  # If the tile moved is in the list of possible moves of the tile clicked
                    if self.pieces.Promotion_Pawn(dico_board[self.player_tile_clicked][0],
                                                  self.player_tile_moved):  # If the player has done a promotion (Pawn at the last line)
                        self.pieces.PromotePawn_into_Queen(dico_board[self.player_tile_clicked][0],
                                                           self.player_tile_moved)  # Promote the pawn into a queen
                        self.piece_moved = dico_board[self.player_tile_moved][0]  # Get the piece moved
                        # Update dico_turn to change the turn because the player has played
                        self.change_turn()

                    else:
                        if dico_board[self.player_tile_moved][2] in [0, - dico_board[self.player_tile_clicked][
                            2]]:  # If the tile moved is a valid move (the tile moved is an empty tile or a tile occupied by an opponent piece))
                            self.pieces.move_piece(dico_board[self.player_tile_clicked][0], self.player_tile_clicked,
                                                   self.player_tile_moved)  # Move the piece and update the dico_board and all the necessary variables
                            self.piece_moved = dico_board[self.player_tile_moved][0]  # Get the piece moved
                            dico_board[self.player_tile_moved][
                                1] = self.save_image_tile_clicked  # Update the image of the tile moved with the image of the tile clicked
                            # Update dico_turn to change the turn because the player has played
                            self.change_turn()

                    # Update the variables to make the colors of the special tiles (clicked_tile, moved_tile)
                    self.list_color_case[1] = self.player_tile_moved
                    self.color_case_waiting = self.player_tile_clicked

                    # Deal with the big update of all piece !
                    self.pieces.possible_moves()  # Update the movement of the pieces on which there are changes about their possibilities of moves
                    if self.pieces.CheckChess(self.piece_moved):  # If the piece put the opponent king in check
                        print("Check")
                        self.pieces.ChessMod_update_possibles_move(
                            self.piece_moved)  # ReUpdate correctly the possibility of the pieces to move and protect the king
                        if self.pieces.Check_Checkmate(self.piece_moved):  # If the king is in checkmate
                            print("END GAME")  # End the game
                    else:
                        self.pieces.ReUpdate_ToNot_OwnChess(
                            self.piece_moved)  # ReUpdate correctly the possibility of the pieces to move and not put their OWN king in check
                    self.pieces.UpdateKingMoves(self.piece_moved)  # Update the king's moves

                    # Allow to make the "En Passant" rule correctly => Must be the turn just after the first move of the opponent pawn to do this rule
                    if self.enter_to_reset_EnPassant:
                        # Reset the old Pawn's object and the enter
                        self.save_pawn_first_move.just_moved = None
                        self.enter_to_reset_EnPassant = False
                    if self.pieces.JustMovedPawn(self.piece_moved):
                        self.enter_to_reset_EnPassant = True
                        self.save_pawn_first_move = self.piece_moved

                else:  # If the tile moved is not in the list of possible moves of the tile clicked
                    # Reset the image of the tile clicked to the initial one
                    dico_board[self.player_tile_clicked][1] = self.save_image_tile_clicked
                    # Rinitialize the color of the tile clicked
                    self.player_tile_clicked = (-1, -1)
                    self.list_color_case[0] = (-1, -1)

            # Update the screen
            pygame.display.update()