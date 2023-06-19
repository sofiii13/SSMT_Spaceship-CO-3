import random
from game.components.enemies.enemy import Enemy
#from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
    
    
    def update(self, game):
        if not self.enemies:
            enemy_variant = random.randint(1, 3)
            self.enemies.append(Enemy(enemy_variant))
            
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        if enemy.rect.colliderect(game.player.rect):
            game.playing = False
            game.death_count += 1
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def reset(self):
        self.enemies =[]
        