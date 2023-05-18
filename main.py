import pygame

from src.app import app
from src.components.menu import Menu

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN)
run = True
hiPoints = 0

while run:
    run = menu.restartScreen()
    
    if run:
        hiPoints = app(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, hiPoints)
    print(hiPoints)