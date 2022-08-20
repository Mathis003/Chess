import math
import pygame
from Configs import *
from Assets import button_sound_on, button_sound_off, button_sound_rect,\
                   button_changes_boardcolor, button_changes_boardcolor_rect

class Button:

    def __init__(self, screen):
        self.screen = screen
        self.sound_on = True

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
