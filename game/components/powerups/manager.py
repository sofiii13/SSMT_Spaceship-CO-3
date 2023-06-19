import pygame
import random
from game.components.powerups.shield import Shield
from game.components.powerups.invisible import Invisible
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_INVISIBLE, DEFAULT_TYPE, SPACESHIP

class Manager:
    def __init__(self):
        self.power_up = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(2, 5)
        
    def generate_power_up(self):
        power_up_type = random.choice([Shield, Invisible])
        power_up = power_up_type()
        self.when_appears += random.randint(10000, 15000)
        self.power_up.append(power_up)
        
    def update(self, game):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_up) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
            
        for power_up in self.power_up:
            power_up.update(game.game_speed, self.power_up)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration * 2000)
                if power_up.type == "shield":
                    game.player.set_image((67, 75), SPACESHIP_SHIELD)
                elif power_up.type == "invisible":
                    game.player.set_image((67, 75), SPACESHIP_INVISIBLE)
                self.power_up.remove(power_up)
    
        # Verificar si el power-up del jugador ha expirado
        if game.player.has_power_up and current_time >= game.player.power_up_time:
            game.player.has_power_up = False
            game.player.power_up_type = DEFAULT_TYPE
            game.player.set_image((60, 40), SPACESHIP)

    def draw(self, screen):
        for power_up in self.power_up:
            power_up.draw(screen)
            
    def reset(self):
        now = pygame.time.get_ticks()
        self.power_up = []
        self.when_appears = random.randint(now + 10000, now + 15000)

