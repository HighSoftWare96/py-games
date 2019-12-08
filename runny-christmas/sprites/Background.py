from helpers.loaders import load_image
from helpers.config import config
from pygame import Surface
from helpers.colors import WHITE

SCREEN_SIZE = config['SCREEN_SIZE']

class Background():
    def __init__(self):
        self.layer0, self.layer0_rect = load_image('background0.png', SCREEN_SIZE)

        self.layer1, self.layer1_rect = load_image('background1.png', SCREEN_SIZE, 0.8)
        self.layer1Offset = 0
        self.layer1Step = 3

        self.layer2, self.layer2_rect = load_image('background2.png', SCREEN_SIZE, 0.3)
        self.layer2Offset = -35
        self.layer2Step = 1

        self.background = Surface(SCREEN_SIZE)
        self.background = self.background.convert()
        self.background.fill(WHITE)
        self._updateImages()

    def getSurf(self):
        self._updateImages()
        return self.background

    def getCoords(self):
        return (0,0)

    def _updateImages(self):
        self.background.blit(self.layer0, (0,0))
        self.background.blit(self.layer1, (0 - self.layer1Offset,80))
        self.background.blit(self.layer1, (SCREEN_SIZE[0] - self.layer1Offset,80))
        self.layer1Offset = (self.layer1Offset + self.layer1Step) % SCREEN_SIZE[0]
        self.background.blit(self.layer2, (0 - self.layer2Offset,80))
        self.background.blit(self.layer2, (SCREEN_SIZE[0] - self.layer2Offset,80))
        self.layer2Offset = (self.layer2Offset + self.layer2Step) % SCREEN_SIZE[0]
