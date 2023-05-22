class Dead:

    def __init__(self, player):
        self.player = player
        
    def check(self, obstacles):
        if obstacles.obstacles and self.player.dino_rect.colliderect(obstacles.obstacles[0].rect):
            self.player.dino_dead = True
            return True
        return False
