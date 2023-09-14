import math
from src.assets import *
from src.piece import Piece

class Game:

    def __init__(self, screen, board, sound_button, board_color_button):

        self.screen = screen
        self.board = board
        self.sound_button = sound_button
        self.board_color_button = board_color_button

        self.piece = Piece(None, None, [], [None, None], 0, True)

        self.white_turn = True
        self.mouse_just_released = False
        self.mouse_pressed = False

        self.running = True
        self.begin_menu = True
        self.end_menu = False
        self.image_piece_selected = 0 # Type of pieces selected (for the images)
        
        self.IA = False

        self.pressed_piece_image = None  # Save the image of the pressed piece (to play) => will be reset the next turn
        self.piece_moved = None  # Save the instance of the piece that has been moved => will be reset the next turn

        # None is out of the screen => will be immediatly update when the game begin
        self.tile_pressed = None
        self.tile_moved = None

        # To draw the color of the tiles where the player moves (before and after)
        self.list_colors_player = [None, None]
        self.color_player = None

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
                    piece = self.piece.get_board_pieces()[tile_clicked[0]][tile_clicked[1]]
                    if ((math.sqrt((initial_pos_mouse[0] - (2 + button_sound_on.get_width() / 2)) ** 2 + (initial_pos_mouse[1] - (2 + button_sound_on.get_width() / 2)) ** 2) > SIZE_SQUARE / 4) and \
                        (math.sqrt((initial_pos_mouse[0] - (self.screen.get_width() - button_changes_boardcolor.get_width() / 2 - 2)) ** 2 + (initial_pos_mouse[1] - 2) ** 2) > SIZE_SQUARE / 4)):
                        if (piece != None):
                            if (self.white_turn and (piece.color == 1)) or \
                                (not self.white_turn and (piece.color == -1)):

                                self.tile_pressed = tile_clicked
                                self.list_colors_player[0] = tile_clicked
                                self.pressed_piece_image = piece.image
                                piece.image = None
                                self.mouse_just_released = True
                    else:
                        self.board_color_button.buttonUpdateClick(initial_pos_mouse)
                        self.sound_button.buttonUpdateClick(initial_pos_mouse)
        
    def display_menu(self):
        self.board.draw_board(self.board_color_button.mod_board)
        self.board.draw_pieces(self.piece.get_list_black_pieces() + self.piece.get_list_white_pieces())
        self.screen.blit(player_1, player_1_rect_1)
        self.screen.blit(player_2, player_2_rect)
        self.screen.blit(player_1, player_1_rect_2)
        self.screen.blit(button_play, button_play_rect_1)
        self.screen.blit(button_play, button_play_rect_2)
    
    def display_game(self):
        self.board.draw_board(self.board_color_button.mod_board)
        if self.list_colors_player[0] != None:
            self.board.draw_tile(self.list_colors_player[0], COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        if self.list_colors_player[1] != None:
            self.board.draw_tile(self.list_colors_player[1], COLORS_MOVES_BOARD[self.board_color_button.mod_board][False])
        if self.color_player != None:
            self.board.draw_tile(self.color_player, COLORS_MOVES_BOARD[self.board_color_button.mod_board][True])
        if self.tile_pressed != None:
            self.board.draw_possible_moves(self.piece.get_board_pieces()[self.tile_pressed[0]][self.tile_pressed[1]].available_moves)
        self.board.draw_pieces(self.piece.get_list_black_pieces() + self.piece.get_list_white_pieces())

        mouse_pos = pygame.mouse.get_pos()
        self.board_color_button.activateFunctionButton(mouse_pos)
        self.sound_button.activateFunctionButton(mouse_pos)

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
                        if ((self.tile_pressed != None) and (self.pressed_piece_image != None)):
                            pos_mouse = pygame.mouse.get_pos()
                            self.screen.blit(self.pressed_piece_image, (pos_mouse[0] - SIZE_SQUARE / 2, pos_mouse[1] - SIZE_SQUARE / 2))

                    # If the player has finished to play and has released the mouse (until the player press the mouse again)
                    if not self.mouse_pressed and self.mouse_just_released:
                        self.mouse_just_released = False
                        final_pos_mouse = pygame.mouse.get_pos()
                        self.tile_moved = (final_pos_mouse[1] // SIZE_SQUARE, final_pos_mouse[0] // SIZE_SQUARE)

                        # If the tile moved is in the list of possible moves of the tile clicked
                        piece = self.piece.get_board_pieces()[self.tile_pressed[0]][self.tile_pressed[1]]
                        if self.tile_moved in piece.available_moves:

                            mod_of_move = piece.move_piece(self.tile_pressed, self.tile_moved, self.image_piece_selected)
                            self.piece_moved = piece
                            self.piece_moved.image = self.pressed_piece_image

                            self.white_turn = not self.white_turn

                            self.list_colors_player[1] = self.tile_moved
                            self.color_player = self.tile_pressed

                            self.piece.update_available_moves(self.piece_moved)
                            
                            # If the piece put the opponent king in check
                            if self.piece.opponent_check(self.piece_moved):
                                mod_of_move = "check"
                                if not self.piece.defend_checked_king(-self.piece_moved.color):
                                    mod_of_move = "checkmate"
                                    self.end_menu = True
                            else:
                                if self.piece.stalemate(self.piece_moved):
                                    mod_of_move = "stalemate"
                                    self.end_menu = True

                            self.play_music(mod_of_move)
                            self.tile_pressed = None

                        # If the tile moved is not in the list of possible moves of the tile clicked
                        else:
                            piece.image = self.pressed_piece_image
                            self.tile_pressed = None
                            self.list_colors_player[0] = None

                if self.IA:
                    pass
            
            # If the player is in the end menu
            else:
                pass

            pygame.display.update()