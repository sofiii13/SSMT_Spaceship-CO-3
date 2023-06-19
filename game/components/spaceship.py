import pygame
import random
import pygame.mixer
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_TYPE, DEFAULT_TYPE, BULLETS_SING_ENEMY

class Spaceship:
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.shooting_time = random.randint(40, 60)
        self.type = SPACESHIP_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0

    def update(self, user_input, game):
        current_time = pygame.time.get_ticks()

        if not self.has_power_up or current_time - self.power_up_time < 10000:
            if user_input[pygame.K_a]:
                self.move_left()
            elif user_input[pygame.K_d]:
                self.move_right()
            elif user_input[pygame.K_w]:
                self.move_up()
            elif user_input[pygame.K_s]:
                self.move_down()
            elif user_input[pygame.K_z]:
                self.fire_bullet(game.bullet_manager)
              
            
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0
            
    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT //  2:
            self.rect.y -= 10
            
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT - 50:
            self.rect.y += 10
            
    def fire_bullet(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
        print(len(bullet_manager.spaceship_bullets))
        sound = pygame.mixer.Sound(BULLETS_SING_ENEMY)
        pygame.mixer.Sound.play(sound)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_image(self, size=(40, 60), image=SPACESHIP):
        self.image = pygame.transform.scale(image, size)

