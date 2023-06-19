import pygame
import pygame.mixer
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
INVISIBLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/invisible.png'))
BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/fonespacial.png'))
ASTEROID = pygame.image.load(os.path.join(IMG_DIR, 'Other/asteroide.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
BULLETS_SING_ENEMY = os.path.join(IMG_DIR,"Other/cancion2.mp3")

DEFAULT_TYPE = "default"
INVISIBLE_TYPE = 'invisible'
SHIELD_TYPE = 'shield'
ENEMY_TYPE = 'enemy'
SPACESHIP_TYPE = 'spaceship'
PLAYER_TYPE = 'player'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_INVISIBLE = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_invisible.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

FONT_STYLE = 'freesansbold.ttf'
STAR_SOUND = os.path.join(IMG_DIR, 'Other/cancion1.mp3')
# Initialize pygame mixer
pygame.mixer.init()

# Load and play the music file


# Rest of your code...

