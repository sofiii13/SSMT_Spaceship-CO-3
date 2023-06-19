import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE
from game.utils.constants import SPACESHIP_TYPE
from game.utils.constants import SHIELD_TYPE, INVISIBLE_TYPE
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class BulletManager:
    def __init__(self):
        self.enemy_bullets: list[Bullet] = []
        self.spaceship_bullets: list[Bullet] = []
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE and game.player.power_up_type != INVISIBLE_TYPE:
                    game.playing = False
                    if not game.player.has_power_up:
                        game.death_count += 1
                    pygame.time.delay(1000)
                break                
        for bullet in self.spaceship_bullets:
            bullet.update(self.spaceship_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.spaceship_bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 1
                    break 
            
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.spaceship_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == SPACESHIP_TYPE and not self.spaceship_bullets:
            self.spaceship_bullets.append(bullet)
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)

