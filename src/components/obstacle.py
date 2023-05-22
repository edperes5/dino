class Obstacle:

    def __init__(self, data, type, SCREEN_WIDTH, SCREEN):
        self.image = data["images"]
        self.anim = data["anim"]
        self.index = 0
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = data["y"]
        self.SCREEN = SCREEN

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            return False
        return True

    def draw(self):
        self.SCREEN.blit(self.image[self.type], self.rect)
        
    def animate(self):
        if self.index >= 9:
            self.index = 0
        self.SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1