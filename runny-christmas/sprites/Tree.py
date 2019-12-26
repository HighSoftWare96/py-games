from pygame.sprite import Sprite
from pygame.mask import from_surface
from helpers.loaders import load_image
from helpers.config import config

SPRITE_CONFIG = config['SPRITES']['TREE']


class Tree(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image, self.rect = load_image('tree.png', SPRITE_CONFIG['SIZE'])
        self.mask = from_surface(self.image)
        self.xProgress = config['SCREEN_SIZE'][0] + 300
        self._positionate()

    def update(self, multiplier = 1):
        self.xProgress -= (config['PX_STEP'] * multiplier)
        self._positionate()

    def isOffscreen(self):
        if self.rect.bottomright[0] < 0:
            self.kill()
            return True
        return False

    def _positionate(self):
        self.rect.bottomright = (self.xProgress, config['GROUND_POSITION'])
