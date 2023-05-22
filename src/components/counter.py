import pygame
from decimal import Decimal

pygame.font.init()

step = Decimal("0.05")

class Counter:

    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.points = 0
        self.font = pygame.font.SysFont(None, 20)

    def startСounter(self, hiPoints):
        text = self.font.render(
            "HI: " + str(round(hiPoints)) + " / " + str(round(self.points)),
            True, (0, 0, 0))
        self.SCREEN.blit(text, (20, 40))
        
        self.points += step
        return self.points
