import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500

    def update(self, user_input):
        if user_input[pygame.K_a]:
            self.move_left()
            print(user_input)
        elif user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_s]:
            self.move_down()
            
    def move_left(self):
        print("left")
        if self.rect.left > 50:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width
    
    def move_right(self):
        print("right")
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0
            
    def move_up(self):
        print("up")
        if self.rect.top > SCREEN_HEIGHT //  2:
            self.rect.y -= 10
            
    def move_down(self):
        print("down")
        if self.rect.bottom < SCREEN_HEIGHT - 50:
            self.rect.y += 10
        
    def draw(self, screen):
        jls_extract_var = (self.rect.x, self.rect.y)
        screen.blit(self.image, self.rect)

