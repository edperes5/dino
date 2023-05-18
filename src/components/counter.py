import pygame

pygame.font.init()


class Counter:

    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.points = 0
        self.font = pygame.font.SysFont(None, 20)

    def startСounter(self, hiPoints, game_speed):
        text = self.font.render(
            "HI: " + str(round(hiPoints)) + " / " + str(round(self.points)),
            True, (0, 0, 0))
        self.SCREEN.blit(text, (20, 40))

        self.points += 0.1
        return self.points
