import pygame
import os
import random

from .obstacle import Obstacle

obstaclesData = [
    # SmallCactus
    {
        "images": [
            pygame.image.load(
                os.path.join("src/assets/Cactus", "SmallCactus1.png")),
            pygame.image.load(
                os.path.join("src/assets/Cactus", "SmallCactus2.png")),
            pygame.image.load(
                os.path.join("src/assets/Cactus", "SmallCactus3.png"))
        ],
        "y": 325,
        "anim": False
    },
    # BigCactus
    {
        "images": [
            pygame.image.load(
                os.path.join("src/assets/Cactus", "LargeCactus1.png")),
            pygame.image.load(
                os.path.join("src/assets/Cactus", "LargeCactus2.png")),
            pygame.image.load(
                os.path.join("src/assets/Cactus", "LargeCactus3.png"))
        ],
        "y": 300,
        "anim": False
    },
    # Bird
    {
        "images": [
            pygame.image.load(os.path.join("src/assets/Bird", "Bird1.png")),
            pygame.image.load(os.path.join("src/assets/Bird", "Bird2.png"))
        ],
        "y": 250,
        "anim": True
    }
]


class Obstacles:

    def __init__(self, SCREEN_WIDTH, game_speed, SCREEN, player):
        self.obstacles = []
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.game_speed = game_speed
        self.SCREEN = SCREEN

    def generate(self):
        obstacleData = obstaclesData[random.randint(0, len(obstaclesData) - 1)]
        self.obstacles.append(Obstacle(obstacleData, random.randint(0, len(obstacleData["images"]) - 1), self.SCREEN_WIDTH, self.SCREEN))

    def update(self):
        if len(self.obstacles) == 0:
            self.generate()

    def draw(self):
        for obstacle in self.obstacles:
            if obstacle.anim:
                obstacle.animate()
            else:
                obstacle.draw()
                
            obstacleStatus = obstacle.update(self.game_speed)
            if not obstacleStatus:
                self.obstacles.pop(0)
