import pygame

from src.components.dinosaur import Dinosaur
from src.components.obstacles import Obstacles
from src.components.counter import Counter
from src.components.background import Background
from src.components.dead import Dead

GAME_SPEED = 10


def app(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, hiPoints):
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
                run = False

        userInput = pygame.key.get_pressed()

        obstacles.update()
        obstacles.draw()

        run = not dead.check(obstacles)

        player.update(userInput)
        player.draw()

        points = counter.startСounter(hiPoints, game_speed)

        if hiPoints < points:
            hiPoints = points

        if points % 100 == 0:
            game_speed += 1

        background.draw()

        clock.tick(30)
        pygame.display.update()

    return hiPoints