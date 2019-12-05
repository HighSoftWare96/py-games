from pygame.sprite import Sprite
from helpers.loaders import load_image
from helpers.config import config


class Tree(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image, self.rect = load_image('tree.png')
        self.xProgress = config['SCREEN_SIZE'][0] + 300
        self._positionate()

    def update(self, multiplier = 1):
        self.xProgress -= (5 * multiplier)
        self._positionate()

    def _positionate(self):
        self.rect.bottomright = (self.xProgress, config['GROUND_POSITION'])
