import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500


    def update(self, user_imput):
        if user_imput[pygame.K_LEFT]:
            self.move_left()
        elif user_imput[pygame.K_RIGHT]:
            self.move_right()
        elif user_imput[pygame.K_UP]:
            self.move_up()
        elif user_imput[pygame.K_DOWN]:
            self.move_down()
            
    def move_left(self):
        if self.rect.left > 50:
            self.rect.x -= 10
    
    def move_right(self):
        if self.rect.right > SCREEN_WIDTH - 50:
            self.rect.x += 10
            
    def move_up(self):
        if self.rect.y > SCREEN_HEIGT // 2:
            self.rect.y -= 10
            
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50: 
            self.rect.y += 10             
        
        


    def draw(self, screen):
        jls_extract_var = (self.rect.x, self.rect.y)
        screen.blit(self.image, jls_extract_var)
        