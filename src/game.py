import math
from src.all_configs.configs import *
from src.all_pieces import Pawn
from src.all_configs.variables import *

class Game:

    def __init__(self, screen, board, pieces, sound_button, board_color_button, IA_Player):

        self.screen = screen
        self.board = board
        self.pieces = pieces # To remove at the end
        self.sound_button = sound_button
        self.board_color_button = board_color_button
        self.IA_Player = IA_Player

        self.dico_turn = {"turn_white": True, "turn_black": False}
        self.mouse_just_released = False # Allow to not click after drop the mouse's pression on a random tile and move the Rect on the image of the piece just before (If True = pressed mouse and Rect's moving, if False = no pressing mouse and Rect's not moving)
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
                    self.board.change_image(self.image_piece_selected)
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

                                self.player_tile_clicked = tile_clicked
                                self.list_color_case[0] = tile_clicked
                                self.save_image_tile_clicked = dico_board[self.player_tile_clicked][1]
                                self.mouse_just_released = True
                                dico_board[self.player_tile_clicked][1] = None
                    else:
                        self.board_color_button.buttonUpdateClick(initial_pos_mouse)
                        self.sound_button.buttonUpdateClick(initial_pos_mouse)
        
    def display_menu(self):
        self.board.draw_board(self.board_color_button.mod_board)
        self.board.draw_pieces()
        self.screen.blit(player_1, player_1_rect_1)
        self.screen.blit(player_2, player_2_rect)
        self.screen.blit(player_1, player_1_rect_2)
        self.screen.blit(button_play, button_play_rect_1)
        self.screen.blit(button_play, button_play_rect_2)
    
    def display_game(self):
        self.board.draw_board(self.board_color_button.mod_board)
        self.board.draw_tile(self.list_color_case[0], COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        self.board.draw_tile(self.list_color_case[1], COLORS_MOVES_BOARD[self.board_color_button.mod_board][False])
        self.board.draw_tile(self.color_case_waiting, COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        self.board.draw_possible_moves(self.player_tile_clicked)
        self.board.draw_pieces()

        mouse_pos = pygame.mouse.get_pos()
        self.board_color_button.activateFunctionButton(mouse_pos)
        self.sound_button.activateFunctionButton(mouse_pos)
    
    def change_turn_player(self):
        self.dico_turn["turn_white"] = not self.dico_turn["turn_white"]
        self.dico_turn["turn_black"] = not self.dico_turn["turn_black"]

    def run(self):

        while self.running:

            # If the player is in the menu
            if self.begin_menu:
                self.events_menu()
                self.display_menu()
            
            # If the player is in the game
            elif not self.end_menu:

                # If the player doesn't play against the IA
                if not self.IA:
                    self.events_game_without_IA()
                    self.display_game()

                    self.mouse_pressed = pygame.mouse.get_pressed()[0]

                    # If the player is playing and choose a tile to move (the mouse is pressed)
                    if self.mouse_pressed and self.mouse_just_released:
                        if ((self.player_tile_clicked != (-1, -1)) and (self.save_image_tile_clicked != None)):
                            pos_mouse = pygame.mouse.get_pos()
                            self.screen.blit(self.save_image_tile_clicked, (pos_mouse[0] - SIZE_SQUARE / 2, pos_mouse[1] - SIZE_SQUARE / 2))

                    # If the player has finished to play and has released the mouse (until the player press the mouse again)
                    if not self.mouse_pressed and self.mouse_just_released:
                        self.mouse_just_released = False
                        final_pos_mouse = pygame.mouse.get_pos()
                        self.player_tile_moved = (final_pos_mouse[1] // SIZE_SQUARE, final_pos_mouse[0] // SIZE_SQUARE)

                        # If the tile moved is in the list of possible moves of the tile clicked

                        if self.player_tile_moved in dico_board[self.player_tile_clicked][3]:
                            mod_of_move = dico_board[self.player_tile_clicked][0].move_piece(self.player_tile_clicked, self.player_tile_moved, self.image_piece_selected)
                            self.piece_moved = dico_board[self.player_tile_moved][0]

                            # If the piece moved is a queen and had been promoted
                            if isinstance(self.piece_moved, type(queen_white)) and self.piece_moved.promoted:
                                self.piece_moved.promoted = False
                            else:
                                dico_board[self.player_tile_moved][1] = self.save_image_tile_clicked

                            self.change_turn_player()

                            self.list_color_case[1] = self.player_tile_moved
                            self.color_case_waiting = self.player_tile_clicked

                            self.pieces.basics_possible_moves(self.piece_moved)
                            enter, piece_that_check = self.pieces.CheckOpponent(self.piece_moved, self.player_tile_clicked)
                            # If the piece put the opponent king in check
                            if enter:
                                mod_of_move = "check"
                                self.pieces.CheckMod_reupdate_possibles_move(piece_that_check)
                                # If the opponent player can play at least one piece
                                if self.pieces.Check_NoMoveAvailable(piece_that_check):
                                    mod_of_move = "checkmate"
                                    self.end_menu = True
                            else:
                                self.pieces.ReUpdate_ToNot_OwnChess(self.piece_moved)
                                # If the opponent player can play at least one piece
                                if self.pieces.Check_NoMoveAvailable(self.piece_moved):
                                    mod_of_move = "stalemate"
                                    self.end_menu = True

                            self.play_music(mod_of_move)

                            if self.enter_to_reset_EnPassant:
                                self.save_pawn_first_move.just_moved = None
                                self.enter_to_reset_EnPassant = False

                            if isinstance(self.piece_moved, type(Pawn((6, 0), 1, True))):
                                if self.piece_moved.just_moved:
                                    self.enter_to_reset_EnPassant = True
                                    self.save_pawn_first_move = self.piece_moved

                            self.player_tile_clicked = (-1, -1)

                        # If the tile moved is not in the list of possible moves of the tile clicked
                        else:
                            dico_board[self.player_tile_clicked][1] = self.save_image_tile_clicked
                            self.player_tile_clicked = (-1, -1)
                            self.list_color_case[0] = (-1, -1)

                if self.IA:
                    pass
            
            # If the player is in the end menu
            else:
                pass

            pygame.display.update()