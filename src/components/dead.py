class Dead:

    def __init__(self, player):
        self.player = player
        
    def check(self, obstacles):
        obstacle = obstacles.obstacles[0]
        
        if obstacle and self.player.dino_rect.colliderect(obstacle.rect):
            self.player.dino_dead = True
            return True
        return False
