from game.components.powerups.power_up import PowerUp
from game.utils.constants import INVISIBLE, INVISIBLE_TYPE, SPACESHIP_INVISIBLE

class Invisible(PowerUp):
    def __init__(self):
        super().__init__(INVISIBLE, INVISIBLE_TYPE)
        
    def activate(self, game):
        game.player.set_image((67, 75), SPACESHIP_INVISIBLE)
        