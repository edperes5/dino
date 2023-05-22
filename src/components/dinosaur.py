import pygame
import os


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 345
    JUMP_VEL = 5

    run_img = [
        pygame.image.load(os.path.join("src/assets/Dino", "DinoRun1.png")),
        pygame.image.load(os.path.join("src/assets/Dino", "DinoRun2.png"))
    ]
    jump_img = pygame.image.load(os.path.join("src/assets/Dino", "DinoJump.png"))
    duck_img = [
        pygame.image.load(os.path.join("src/assets/Dino", "DinoDuck1.png")),
        pygame.image.load(os.path.join("src/assets/Dino", "DinoDuck2.png"))
    ]
    dead_img = pygame.image.load(os.path.join("src/assets/Dino", "DinoDead.png"))

    def __init__(self, SCREEN):
        self.screen = SCREEN
        self.jump_vel = self.JUMP_VEL
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_dead = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_run:
            self.run()

        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.duck()
        
        if self.dino_dead:
            self.image = self.dead_img
            
            if self.dino_duck:
                self.dino_rect.x = self.X_POS
                self.dino_rect.y = self.Y_POS

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 2.5
            self.jump_vel -= 0.15
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self):
        self.screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))