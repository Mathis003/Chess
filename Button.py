import math
import pygame
from Configs import *
from Assets import button_sound_on, button_sound_off, button_sound_rect, button_changes_boardcolor,\
    button_changes_boardcolor_rect, move_sound, capture_sound, castling_sound, stalemate_sound, check_sound,\
    checkmate_sound

class Button:

    def __init__(self, screen):
        self.screen = screen
        self.sound_on = True
        self.mod_board = "blue_mod"

    def setSound(self, initial_pos_mouse):
        # Deal with the sound and his variable
        if math.sqrt((initial_pos_mouse[0] - (2 + button_sound_on.get_width() / 2)) ** 2 + (
                initial_pos_mouse[1] - (2 + button_sound_on.get_width() / 2)) ** 2) <= SQUARE / 4:
            if button_sound_rect.collidepoint(initial_pos_mouse):
                if self.sound_on:
                    self.sound_on = False
                else:
                    self.sound_on = True

    def activateSoundButton(self, mouse_pos):
        # Deal with the button of the sound
        if math.sqrt((mouse_pos[0] - (2 + button_sound_on.get_width() / 2)) ** 2 + (
                mouse_pos[1] - (2 + button_sound_on.get_width() / 2)) ** 2) <= SQUARE / 4 and not \
                pygame.mouse.get_pressed()[0]:  # If the mouse is on the circle of the button
            if self.sound_on:
                pygame.draw.circle(self.screen, (255, 255, 255), (2 + button_sound_on.get_width() / 2,
                                    2 + button_sound_on.get_width() / 2), SQUARE / 4)
                self.screen.blit(button_sound_on, button_sound_rect)  # Draw the button of the sound pressed
            if not self.sound_on:
                pygame.draw.circle(self.screen, (255, 255, 255), (2 + button_sound_on.get_width() / 2,
                                    2 + button_sound_on.get_width() / 2), SQUARE / 4)
                self.screen.blit(button_sound_off, button_sound_rect)

    def activateChangeColorButton(self, mouse_pos):
        # Deal with the button to change board's colors
        if math.sqrt((mouse_pos[0] - (self.screen.get_width() - button_changes_boardcolor.get_width() / 2 - 2))
                     ** 2 + (mouse_pos[1] - 2) ** 2) <= SQUARE / 4 and not pygame.mouse.get_pressed()[0]: # If the mouse is on the circle of the button
            pygame.draw.circle(self.screen, (255, 255, 255), (self.screen.get_width() - 2 -
                                button_changes_boardcolor.get_width() / 2, 2 + button_changes_boardcolor.get_height() / 2), SQUARE / 4)
            self.screen.blit(button_changes_boardcolor, button_changes_boardcolor_rect)  # Draw the button of the sound pressed
    def launch_music(self, mod_of_move):
        if mod_of_move == "move":
            move_sound.play()
        elif mod_of_move == "capture":
            capture_sound.play()
        elif mod_of_move == "check":
            check_sound.play()
        elif mod_of_move == "castling":
            castling_sound.play()
        elif mod_of_move == "checkmate":
            checkmate_sound.play()
        elif mod_of_move == "stalemate":
            stalemate_sound.play()

    def play_music(self, mod_of_move):
        if self.sound_on:
            self.launch_music(mod_of_move)
    def setMod(self, initial_pos_mouse):
        # Deal with the mod of the board and his variable
        if math.sqrt((initial_pos_mouse[0] - (self.screen.get_width() - button_changes_boardcolor.get_width() / 2 - 2))
                     ** 2 + (initial_pos_mouse[1] - 2) ** 2) <= SQUARE / 4:  # If the mouse is on the circle of the button
            if self.mod_board == "brown_mod":
                self.mod_board = "blue_mod"
            elif self.mod_board == "blue_mod":
                self.mod_board = "green_mod"
            elif self.mod_board == "green_mod":
                self.mod_board = "brown_mod"