import pygame

from src.components.dinosaur import Dinosaur
from src.components.obstacles import Obstacles
from src.components.counter import Counter
from src.components.background import Background
from src.components.dead import Dead
from src.components.menu import Menu

pygame.init()

GAME_SPEED = 5
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill((255, 255, 255))

menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN)
run = True
hiPoints = 0

def main(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, hiPoints):
    run = True
    clock = pygame.time.Clock()

    game_speed = GAME_SPEED

    player = Dinosaur(SCREEN)
    obstacles = Obstacles(SCREEN_WIDTH, game_speed, SCREEN, player)
    dead = Dead(player)
    background = Background(SCREEN, game_speed)
    counter = Counter(SCREEN) 

    while run:
        SCREEN.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        userInput = pygame.key.get_pressed()

        obstacles.update()
        obstacles.draw()

        run = not dead.check(obstacles)

        player.update(userInput)
        player.draw()

        points = counter.startСounter(hiPoints)

        if hiPoints < points:
            hiPoints = points

        if points > 0 and points % 100 == 0:
            game_speed += 1
            obstacles.game_speed = game_speed
            background.game_speed = game_speed

        background.draw()

        clock.tick(60)
        pygame.display.update()

    return hiPoints

while run:
    run = menu.restartScreen()
    
    if run:
        hiPoints = main(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, hiPoints)
