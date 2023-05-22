import pygame

pygame.font.init()


class Menu:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN = SCREEN
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render("Press any Key to Start", True, (0, 0, 0))

    def restartScreen(self):
        textRect = self.text.get_rect()
        textRect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)

        self.SCREEN.blit(self.text, textRect)
        
        while True:
            pygame.display.update()

            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    return True
