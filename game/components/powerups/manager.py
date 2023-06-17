import random
import pygame
from game.components.powerups.shield import Shield

class Manager(self):
    def __init__(self):
        self.power_up = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(2, 5)
        
    def generate_power_up(self):
        shield = Shield()
        self.power_ups.append(shield)
        
    def update(self):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
            
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect
            
    def draw(self,screen):
        for power_up in self.power_up:
                    
        