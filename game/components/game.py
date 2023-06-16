import pygame

from game.components.you_died import YouDied
from game.components.menu import Menu
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        
        self.score = 0
        self.death_count = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        
        self.menu = Menu("Press enter to start", 32)
        self.max_score = 0  # Agregar el atributo max_score

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.quit()


    def play(self, score):
        self.enemy_manager.reset()
        self.playing = True
        self.score = score
        while self.playing:
            self.events()
            self.update()
            self.draw()
        you_died_screen = YouDied(self.score, self.max_score)
        you_died_screen.run()
        self.reset()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 248, 2))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (244, 218, 4))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)
     
    def show_menu(self):
        if self.death_count > 0:
            self.menu.update_message("GAME OVER")

        self.menu.draw(self.screen)
        self.menu.events(self.on_close, lambda: self.play(0))  # Pasar la puntuación como argumento
        
        
    def on_close(self):
        self.playing = False
        self.running = False    
        
    def reset(self):
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.score = 0
        if self.score > self.max_score:
            self.max_score = self.score
        self.death_count = 0
        self.playing = False
        self.score = 0
        self.death_count += 1
        self.enemy_manager.reset()
        if self.score > self.max_score:
            self.max_score = self.score
        
        
    def show_menu(self):
        if self.death_count > 0:
            self.menu.update_message("GAME OVER")
            self.reset()  # Reiniciar el juego antes de mostrar el menú
            self.score = 0  # Reiniciar la puntuación a 0
        
        while not self.playing:
            self.menu.draw(self.screen)
            self.menu.events(self.on_close, self.start_game)
        

    def start_game(self):
        self.play(0)  # Iniciar el juego con una puntuación inicial de 0