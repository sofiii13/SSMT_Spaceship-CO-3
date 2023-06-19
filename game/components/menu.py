import os
import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, ICON, IMG_DIR


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, message, text_size=30):
        pygame.init()
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        
        # Cargar imagen de fondo
        self.background = pygame.image.load(os.path.join(IMG_DIR, 'Other/fonespacial.png'))
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()
        
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        pygame.display.update()
    
    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
