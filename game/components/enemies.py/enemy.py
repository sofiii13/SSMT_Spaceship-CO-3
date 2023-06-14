import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


LEFT ='left'
RIGHT ='right'
class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    
    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_1,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        
        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
    
    def update(self, ships):
        self.rect.y += self.speed_y
        
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
            
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
        self.update.movement()
            
            
    def update_movement(self):
        self.moving_index += 1
        if  self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
            
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
        
        
    def draw(self, screen):
        screen.blit (self.image,(self.rect.x, self.rect.y))