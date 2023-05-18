import pygame
import os

BG = pygame.image.load(os.path.join("src/assets/Other", "Track.png"))


class Background:
    x_pos_bg = 0
    y_pos_bg = 380

    def __init__(self, SCREEN, game_speed):
        self.SCREEN = SCREEN
        self.game_speed = game_speed

    def draw(self):
        image_width = BG.get_width()
        self.SCREEN.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
