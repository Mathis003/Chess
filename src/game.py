from src.assets import *
import math

# TODO : The sound doesn't work except for check !

class Game:

    def __init__(self, screen, piece, IA_player, board, sound_button, board_color_button):

        self.screen = screen
        self.piece = piece
        self.IA_player = IA_player
        self.board = board
        self.sound_button = sound_button
        self.board_color_button = board_color_button

        self.IA = False
        self.turn_IA = False
        self.running = True
        self.begin_menu = True
        self.end_menu = False
        self.white_turn = True
        self.winner = 0

        self.type_image_piece = 0 # Type of pieces selected (for the images)

        self.mouse_pressed = False
        self.mouse_just_released = False

        self.pressed_piece_image = None  # Save the image of the pressed piece (to play) => will be reset the next turn
        self.piece_moved = None  # Save the instance of the piece that has been moved => will be reset the next turn

        # None is out of the screen => will be immediatly update when the game begin
        self.tile_pressed = None
        self.tile_moved = None

        # To draw the color of the tiles where the player moves (before and after)
        self.list_colors_player = [None, None]
        self.color_player = None
    
    def reset_game(self):
        self.white_turn = True
        self.winner = 0
        self.type_image_piece = 0
        self.mouse_pressed = False
        self.mouse_just_released = False
        self.pressed_piece_image = None
        self.piece_moved = None
        self.tile_pressed = None
        self.tile_moved = None
        self.list_colors_player = [None, None]
        self.color_player = None

        import src.variables
        from src.all_pieces import Rook, Queen, King, Pawn, Bishop, Knight

        rook_white_left = Rook((7, 0), 1)
        rook_white_right = Rook((7, 7), 1)
        rook_black_left = Rook((0, 0), -1)
        rook_black_right = Rook((0, 7), -1)

        src.variables.board_pieces = [[rook_black_left, Knight((0, 1), -1), Bishop((0, 2), -1), Queen((0, 3), -1), King((0, 4), -1, rook_black_left, rook_black_right), Bishop((0, 5), -1), Knight((0, 6), -1), rook_black_right],
                        [Pawn((1, 0), -1), Pawn((1, 1), -1), Pawn((1, 2), -1), Pawn((1, 3), -1), Pawn((1, 4), -1), Pawn((1, 5), -1), Pawn((1, 6), -1), Pawn((1, 7), -1)],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [Pawn((6, 0), 1), Pawn((6, 1), 1), Pawn((6, 2), 1), Pawn((6, 3), 1), Pawn((6, 4), 1), Pawn((6, 5), 1), Pawn((6, 6), 1), Pawn((6, 7), 1)],
                        [rook_white_left, Knight((7, 1), 1), Bishop((7, 2), 1), Queen((7, 3), 1), King((7, 4), 1, rook_white_left, rook_white_right), Bishop((7, 5), 1), Knight((7, 6), 1), rook_white_right]]

        src.variables.list_black_pieces = []
        for i in range(0, 2):
            for j in range(8):
                src.variables.list_black_pieces.append(src.variables.board_pieces[i][j])

        src.variables.list_white_pieces = []
        for i in range(6, 8):
            for j in range(8):
                src.variables.list_white_pieces.append(src.variables.board_pieces[i][j])
        
        self.update_moves_first_turn()

    def change_image(self):
        for piece in self.piece.get_list_black_pieces() + self.piece.get_list_white_pieces():
            piece.switch_image(self.type_image_piece)
        self.type_image_piece = 1 - self.type_image_piece

    def play_music(self, mod_of_move):
        if self.sound_button.sound_on:
            MOD_MOVES = {"move" : move_sound, "capture" : capture_sound, "check" : check_sound, "castling" : castling_sound, "checkmate" : checkmate_sound, "stalemate" : stalemate_sound}
            print(MOD_MOVES[mod_of_move])
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
                    self.change_image()

                # If the mouse is clicked on the left button
                elif event.button == 1:
                    initial_pos_mouse = pygame.mouse.get_pos()
                    tile_clicked = (initial_pos_mouse[1] // SIZE_SQUARE, initial_pos_mouse[0] // SIZE_SQUARE)
                    piece = self.piece.get_board_pieces()[tile_clicked[0]][tile_clicked[1]]
                    if ((math.sqrt((initial_pos_mouse[0] - (2 + button_sound_on.get_width() / 2)) ** 2 + (initial_pos_mouse[1] - (2 + button_sound_on.get_width() / 2)) ** 2) > SIZE_SQUARE / 4) and \
                        (math.sqrt((initial_pos_mouse[0] - (self.screen.get_width() - button_changes_boardcolor.get_width() / 2 - 2)) ** 2 + (initial_pos_mouse[1] - 2) ** 2) > SIZE_SQUARE / 4)):
                        if ((piece != None) and (not self.end_menu)):
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

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if self.end_menu:
                        self.end_menu = False
                        self.begin_menu = True
                        self.reset_game()
        
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
    
    def display_winner(self):
        if self.winner == 1:
            winner = "WHITE"
        elif self.winner == -1:
            winner = "BLACK"
        else:
            winner = "DRAW"

        font = pygame.font.Font(None, 120)
        texte = font.render(f"WINNER : {winner}", True, (0, 0, 0))
        texte_rect = texte.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(texte, texte_rect)

        texte = font.render(f"REPLAY : TAP 1", True, (0, 0, 0))
        texte_rect = texte.get_rect(center=(WIDTH // 2, 100 + HEIGHT // 2))
        self.screen.blit(texte, texte_rect)



    def update_moves_first_turn(self):
        for piece in self.piece.get_list_white_pieces():
            piece.update_possible_moves()

    def run(self):
        
        self.update_moves_first_turn()
        while self.running:

            # If the player is in the menu
            if self.begin_menu:
                self.events_menu()
                self.display_menu()
            
            # If the player is in the game
            elif not self.end_menu:

                # If the player doesn't play against the IA
                if (not self.IA) or (not self.turn_IA):
                    self.events_game_without_IA()
                    self.display_game()

                    self.mouse_pressed = pygame.mouse.get_pressed()[0]

                    # If the player is playing and choose a tile to move (the mouse is pressed)
                    if self.mouse_pressed and self.mouse_just_released:

                        # If the player clicked on a valid piece
                        if ((self.tile_pressed != None) and (self.pressed_piece_image != None)):
                            pos_mouse = pygame.mouse.get_pos()
                            self.screen.blit(self.pressed_piece_image, (pos_mouse[0] - SIZE_SQUARE / 2, pos_mouse[1] - SIZE_SQUARE / 2))

                    # If the player has finished to play and has released the mouse (until the player press the mouse again)
                    if not self.mouse_pressed and self.mouse_just_released:

                        self.mouse_just_released = False
                        final_pos_mouse = pygame.mouse.get_pos()
                        self.tile_moved = (final_pos_mouse[1] // SIZE_SQUARE, final_pos_mouse[0] // SIZE_SQUARE)
                        piece_clicked = self.piece.get_board_pieces()[self.tile_pressed[0]][self.tile_pressed[1]]

                        # If the tile_moved is in the list of possible moves of the piece clicked
                        if self.tile_moved in piece_clicked.available_moves:

                            # Move the piece
                            mod_of_move = piece_clicked.move_piece(self.tile_pressed, self.tile_moved, self.type_image_piece)
                            self.piece_moved = piece_clicked

                            ## Update variables ##
                            self.white_turn = not self.white_turn
                            self.piece_moved.image = self.pressed_piece_image
                            self.tile_pressed = None
                            self.list_colors_player[1] = self.tile_moved
                            self.color_player = self.tile_pressed
                            self.turn_IA = True

                            # Update all the available moves for the new player
                            mod_of_move = self.piece.update_available_moves(self.piece_moved)

                            """
                            If the game is over (checkmate or stalemate)
                            - checkmate : the king is in chess and the player can't move any pieces.
                            - stalemate : the king is NOT in chess but the player can't move any pieces.
                            """
                            if mod_of_move == "checkmate" or mod_of_move == "stalemate":
                                if mod_of_move == "checkmate":
                                    if self.white_turn == 0:
                                        self.winner = 1
                                    else:
                                        self.winner = -1
                                self.end_menu = True

                            # Launch the music of the move played
                            self.play_music(mod_of_move)

                        # If the tile_moved isn't in the list of possible moves of the piece clicked
                        else:
                            ## Update variables ##
                            piece_clicked.image = self.pressed_piece_image
                            self.tile_pressed = None
                            self.list_colors_player[0] = None

                if self.IA and self.turn_IA:
                    depth = 3
                    self.IA_player.IA_move(self.piece_moved, depth)
                    pass
            
            # If the player is in the end menu (end game)
            else:
                # TODO
                self.events_game_without_IA()
                self.display_game()
                self.display_winner()

            pygame.display.update()