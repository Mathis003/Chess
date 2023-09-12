import math
from src.all_configs.configs import *
from src.all_pieces import Pawn
from src.all_configs.variables import *

class Game:

    def __init__(self, screen, board, pieces, sound_button, board_color_button, IA_Player):

        self.screen = screen
        self.board = board
        self.pieces = pieces
        self.sound_button = sound_button
        self.board_color_button = board_color_button
        self.IA_Player = IA_Player

        self.dico_turn = {"turn_white": True, "turn_black": False}
        self.enter_mouse_pressed = False # Allow to not click after drop the mouse's pression on a random tile and move the Rect on the image of the piece just before (If True = pressed mouse and Rect's moving, if False = no pressing mouse and Rect's not moving)
        self.mouse_pressed = False

        self.running = True
        self.begin_menu = True
        self.end_menu = False
        self.image_piece_selected = 0 # Type of pieces selected (for the images)
        
        self.IA = True # Boolean to know if the player is playing against the IA or not (True = against IA, False = against player)

        # Initialization of variables that will be directly change ! (Initialyze random value to prevent errors)
        self.enter_to_reset_EnPassant = False  # Allow to reset some stuffs for the "En Passant" move
        self.save_pawn_first_move = None  # Save the object : Pawn that has done, the turn before, his first move => Will be reset the next Turn => Usefull for the "En Passant" rule :)
        self.save_image_tile_clicked = None  # Save the image of the tile clicked => Will be reset the next Turn
        self.piece_moved = None  # Save the object : Piece that has been moved => Will be reset the next Turn

        self.player_tile_clicked = (-1, -1)  # Tile where the player clicked on the board to begin to play (initialize on (-1, -1) to be out of the board without causing error)
        self.player_tile_moved = (-1, -1)  # Tile where the player clicked on the board to move (after playing) (initialize on (-1, -1) to be out of the board without causing error)
        self.list_color_case = [(-1, -1), (-1, -1)]  # List of the color of the case where the player clicked on the board (to have the historic and draw constantly the color until the next player play)
        self.color_case_waiting = (-1, -1)  # Color of the case where the player clicked on the board (to have the historic and draw constantly the color until the next player play)

    def play_music(self, mod_of_move):
        if self.sound_button.sound_on:
            MOD_MOVES[mod_of_move].play()

    def events_menu(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the left mouse button is clicked
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_play_rect_1.collidepoint(mouse_pos):
                        self.IA = False
                        self.begin_menu = False
                    elif button_play_rect_2.collidepoint(mouse_pos):
                        self.IA = True
                        self.begin_menu = False
                    game_start_sound.play()

    def events_game_without_IA(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked on the wheel
                if event.button == 2:
                    self.pieces.change_image(self.image_piece_selected)
                    self.image_piece_selected = abs(1 - self.image_piece_selected)

                # If the mouse is clicked on the left button
                elif ((event.button == 1) and (not self.end_menu)):
                    initial_pos_mouse = pygame.mouse.get_pos()
                    tile_clicked = (initial_pos_mouse[1] // SIZE_SQUARE, initial_pos_mouse[0] // SIZE_SQUARE)

                    if ((math.sqrt((initial_pos_mouse[0] - (2 + button_sound_on.get_width() / 2)) ** 2 + (initial_pos_mouse[1] - (2 + button_sound_on.get_width() / 2)) ** 2) > SIZE_SQUARE / 4) and \
                        (math.sqrt((initial_pos_mouse[0] - (self.screen.get_width() - button_changes_boardcolor.get_width() / 2 - 2)) ** 2 + (initial_pos_mouse[1] - 2) ** 2) > SIZE_SQUARE / 4)):
                        if (dico_board[tile_clicked][0] != None):
                            if (self.dico_turn["turn_white"] and (dico_board[tile_clicked][0].color == 1)) or \
                                (self.dico_turn["turn_black"] and (dico_board[tile_clicked][0].color == -1)):
                                self.update_necessary_variables(tile_clicked)
                    else:
                        self.board_color_button.buttonUpdateClick(initial_pos_mouse)
                        self.sound_button.buttonUpdateClick(initial_pos_mouse)









    def UpdateMovePieces(self, mod_of_move):
        """
        Update all the possibility of moves for both side (with Check,...) => UPDATE mod_of_move if the move is a check,
        checkmate or a stalemate and return it.
        param mod_of_move = mod of the last move ("check" if the last move put the opponent king in Check by example)
        return: mod_of_move
        """
        # Deal with the big update of all piece !
        self.pieces.basics_possible_moves(self.piece_moved)  # Update the movement of the pieces on which there are changes about their possibilities of moves + the specvials moves ("En Passant" and "Castling")
        enter, piece_that_check = self.pieces.CheckOpponent(self.piece_moved, self.player_tile_clicked)  # Check if the player has check the opponent
        if enter:  # If the piece put the opponent king in check
            mod_of_move = "check"
            self.pieces.CheckMod_reupdate_possibles_move(piece_that_check)  # ReUpdate correctly the possibility of the pieces to move and protect the king
            if self.pieces.Check_NoMoveAvailable(piece_that_check):  # Check if the opponent player can play at least one piece
                mod_of_move = "checkmate"
                self.end_menu = True
        else:
            self.pieces.ReUpdate_ToNot_OwnChess(self.piece_moved)  # ReUpdate correctly the possibility of the pieces to move and not put their OWN king in check
            if self.pieces.Check_NoMoveAvailable(self.piece_moved):  # Check if the opponent player can play at least one piece
                mod_of_move = "stalemate"
                self.end_menu = True

        return mod_of_move
    
    ########################
    ### UPDATE FUNCTIONS ###
    ########################

    def display_menu(self):
        """
        Display and draw on the screen all the necessary images, colors,... to make the begin menu's image
        """
        # Draw all the tile on the board
        self.board.draw_board(self.board_color_button.mod_board)
        # Display the pieces on the board (Done at the end of the loop to be sure that the pieces aren't hide by the tiles's color)
        self.board.draw_pieces()
        # Display the player
        self.screen.blit(player_1, player_1_rect_1)
        self.screen.blit(player_2, player_2_rect)
        self.screen.blit(player_1, player_1_rect_2)
        self.screen.blit(button_play, button_play_rect_1)
        self.screen.blit(button_play, button_play_rect_2)
        # Update the screen
        pygame.display.update()

    def UpdateGame(self):
        """
        Update the Game => Display on the screen the new pieces at the right place and the colors of the board
        """
        # Update the elements of the game (board, pieces, ...)
        # Draw all the tile on the board
        self.board.draw_board(self.board_color_button.mod_board)
        # Display the colors of the possible moves / the tile clicked
        self.board.draw_tile(self.list_color_case[0], COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        self.board.draw_tile(self.list_color_case[1], COLORS_MOVES_BOARD[self.board_color_button.mod_board][False])
        self.board.draw_tile(self.color_case_waiting, COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        self.board.draw_possible_moves(self.player_tile_clicked)
        # Display the pieces on the board (Done at the end of the loop to be sure that the pieces aren't hide by the tiles's color)
        self.board.draw_pieces()

    def update_necessary_variables(self, tile_clicked):
        """
        Update some necessary variables to make the game possible
        :param tile_clicked: tile where the player clicked to play
        """
        """Update some necessary variables"""
        self.player_tile_clicked = tile_clicked  # Update the player_tile_clicked
        self.list_color_case[0] = tile_clicked
        self.save_image_tile_clicked = dico_board[self.player_tile_clicked][1]  # Save the image of the tile clicked
        self.enter_mouse_pressed = True
        dico_board[self.player_tile_clicked][1] = None  # Update the image of the piece and replace it by None

    def UpdateEnPassantMove(self):
        """
        Update the enter to the move "EnPassant"
        """
        # Allow to make the "En Passant" rule correctly => Must be the turn just after the first move of the opponent pawn to do this rule
        if self.enter_to_reset_EnPassant:
            # Reset the old Pawn's object and the enter
            self.save_pawn_first_move.just_moved = None
            self.enter_to_reset_EnPassant = False
        if isinstance(self.piece_moved, type(Pawn((6, 0), 1, True))):
            if self.piece_moved.just_moved:
                self.enter_to_reset_EnPassant = True
                self.save_pawn_first_move = self.piece_moved

    def change_turn(self):
        """
        Change the player's turn
        """
        if self.dico_turn["turn_white"]:
            self.dico_turn["turn_white"] = False
            self.dico_turn["turn_black"] = True
        else:
            self.dico_turn["turn_white"] = True
            self.dico_turn["turn_black"] = False

    def ResetBcMoveNotAllowed(self):
        """
        Reset the variables of tile_clicked and save_image_tile_clicked because the move is cancelled !
        """
        # Reset the image of the tile clicked to the initial one
        dico_board[self.player_tile_clicked][1] = self.save_image_tile_clicked
        # Rinitialize the color of the tile clicked
        self.player_tile_clicked = (-1, -1)
        self.list_color_case[0] = (-1, -1)


    def run(self):
        """
        Run the mainloop of the game that call all of the functions at the top
        """
        while self.running:

            # If the player is in the menu
            if self.begin_menu:
                self.events_menu()
                self.display_menu()

            if not self.begin_menu: # If the player is in the game
                if not self.IA:

                    self.events_game_without_IA()

                    if not self.end_menu:
                        self.UpdateGame()
                        mouse_pos = pygame.mouse.get_pos()  # Update the mouse position
                        self.mouse_pressed = pygame.mouse.get_pressed()[0]  # Update the mouse_pressed variable

                        # Activate button function
                        self.board_color_button.activateFunctionButton(mouse_pos)
                        self.sound_button.activateFunctionButton(mouse_pos)

                        # Section use during one of the player plays and keep the mouse pressed to choose a tile to move
                        if self.mouse_pressed and self.enter_mouse_pressed:  # If the mouse is pressed and the enter_mouse_pressed is open (= True)
                            if self.player_tile_clicked != (-1, -1):  # If the player_tile_clicked isn't (-1, -1) => Different of the initialisation
                                pos_mouse = pygame.mouse.get_pos()  # Get the current mouse position (x, y) (usefull to update the rect's position of the piece)
                                if self.save_image_tile_clicked != None:
                                    self.screen.blit(self.save_image_tile_clicked, (pos_mouse[0] - SIZE_SQUARE / 2, pos_mouse[1] - SIZE_SQUARE / 2))  # Update the image of the piece clicked

                        # Section use during one of the player has finished to play and release the mouse to choose a tile to move (until the player press the mouse again)
                        if not self.mouse_pressed and self.enter_mouse_pressed:  # If the mouse is not pressed anymore and the enter_mouse_pressed is open (= True)

                            self.enter_mouse_pressed = False  # Close the enter_mouse_pressed variable to pass this section just ONCE
                            final_pos_mouse = pygame.mouse.get_pos()
                            self.player_tile_moved = (final_pos_mouse[1] // SIZE_SQUARE, final_pos_mouse[0] // SIZE_SQUARE)

                            if self.player_tile_moved in dico_board[self.player_tile_clicked][3]:  # If the tile moved is in the list of possible moves of the tile clicked

                                mod_of_move = self.pieces.move_piece(dico_board[self.player_tile_clicked][0], self.player_tile_clicked, self.player_tile_moved, self.image_piece_selected)  # Move the piece and update the dico_board and all the necessary variables AND save the mod of the move (capture, move)
                                self.piece_moved = dico_board[self.player_tile_moved][0]  # Get the piece moved

                                if isinstance(self.piece_moved, type(queen_white)) and self.piece_moved.promoted:  # If the piece moved is a queen and had been promoted
                                    self.piece_moved.promoted = False  # Set the promoted variable to False
                                else:
                                    dico_board[self.player_tile_moved][1] = self.save_image_tile_clicked  # Update the image of the tile moved with the image of the tile clicked

                                # Update dico_turn to change the turn because the player has played
                                self.change_turn()

                                # Update the variables to make the colors of the special tiles (clicked_tile, moved_tile)
                                self.list_color_case[1] = self.player_tile_moved
                                self.color_case_waiting = self.player_tile_clicked

                                mod_of_move = self.UpdateMovePieces(mod_of_move)

                                self.play_music(mod_of_move)

                                if not self.end_menu:
                                    self.UpdateEnPassantMove()
                                    self.player_tile_clicked = (-1, -1)  # Reset the player_tile_clicked variable

                                else:
                                    self.UpdateGame()

                            else:  # If the tile moved is not in the list of possible moves of the tile clicked
                                self.ResetBcMoveNotAllowed()

                    # If the game is over (DRAW or CHECKMATE)
                    if self.end_menu:
                        pass

                if self.IA:
                    pass

                # Update the screen
                pygame.display.update()