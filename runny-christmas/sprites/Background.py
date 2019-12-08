from helpers.loaders import load_image
from helpers.config import config
from pygame import Surface
from helpers.colors import WHITE

SCREEN_SIZE = config['SCREEN_SIZE']

class Background():
    def __init__(self):
        self.layer0, self.layer0_rect = load_image('background0.png', SCREEN_SIZE)
        self.background = Surface(SCREEN_SIZE)
        self.background = self.background.convert()
        self.background.fill(WHITE)
        self._loadImages()

    def getSurf(self):
        self._loadImages()
        return self.background

    def getCoords(self):
        return (0,0)

    def _loadImages(self):
        self.background.blit(self.layer0, (0,0))
