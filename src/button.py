import math
import pygame
from src.configs import *

class Button:

    def __init__(self, screen, image, rect, center_location):
        self.screen = screen
        self.image = image
        self.rect = rect
        self.center_location = center_location
    
    def checkCollision(self, pos_mouse):
        return (math.sqrt((pos_mouse[0] - self.center_location[0]) ** 2 + (
                           pos_mouse[1] - self.center_location[1]) ** 2) <= SIZE_SQUARE / 4)

    def displayButton(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.center_location, SIZE_SQUARE / 4)
        self.screen.blit(self.image, self.rect)
    

class Sound_Button(Button):

    def __init__(self, screen, image_sound_on, image_sound_off, rect, center_location):
        super().__init__(screen, image_sound_on, rect, center_location)
        self.sound_on_button = Button(screen, image_sound_on, rect, center_location)
        self.sound_off_button = Button(screen, image_sound_off, rect, center_location)
        self.current_button = self.sound_on_button
        self.sound_on = True

    def changeButton(self):
        if self.current_button == self.sound_on_button:
            self.current_button = self.sound_off_button
        else:
            self.current_button = self.sound_on_button
        self.sound_on = not self.sound_on

    def displayButton(self):
        self.current_button.displayButton()
    
    def buttonUpdateClick(self, initial_pos_mouse):
        if self.checkCollision(initial_pos_mouse):
            self.changeButton()

    def activateFunctionButton(self, pos_mouse):
        if self.checkCollision(pos_mouse) and not pygame.mouse.get_pressed()[0]:
            self.displayButton()


class BoardColor_Button(Button):

    def __init__(self, screen, image, rect, center_location):
        super().__init__(screen, image, rect, center_location)
        self.mod_board = "blue_mod"

    def changeColorBoard(self):
        if self.mod_board == "brown_mod":
            self.mod_board = "blue_mod"
        elif self.mod_board == "blue_mod":
            self.mod_board = "green_mod"
        else:
            self.mod_board = "brown_mod"
    
    def buttonUpdateClick(self, initial_pos_mouse):
        if self.checkCollision(initial_pos_mouse):
            self.changeColorBoard()

    def activateFunctionButton(self, pos_mouse):
        if self.checkCollision(pos_mouse) and not pygame.mouse.get_pressed()[0]:
            self.displayButton()