from pygame.locals import *
from helpers.loaders import load_image
from helpers.config import config
from pygame import Surface
from random import randrange

TERRAIN_CONFIG = config['TERRAIN']
TERRAIN_SIZE = TERRAIN_CONFIG['SIZE']

class Terrain():
    def __init__(self):
        self._loadImages()
        self.stopped = True
        self.surface = Surface((config['SCREEN_SIZE'][0], config['SCREEN_SIZE'][1] 
        - config['GROUND_POSITION']))
        self.surface = self.surface.convert()
        self.xOffset = 0

    def getSurf(self, multiplier = 1):
        self._fillWithTextures(multiplier)
        return self.surface

    def start(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def getCoords(self):
        return (0,config['GROUND_POSITION'])

    def _loadImages(self):
        self.backImg, self.backImgRect = load_image('terrain.png',  TERRAIN_SIZE)
        self.foreImg, self.foreImgRect = load_image('terrain_fore.png', TERRAIN_SIZE) 


    def _fillWithTextures(self, multiplier = 1):
        totalXSpace = config['SCREEN_SIZE'][0] + (2 * TERRAIN_SIZE[0])
        for y in range(0, config['SCREEN_SIZE'][1], TERRAIN_SIZE[1]):
            for x in range(-TERRAIN_SIZE[0], totalXSpace, TERRAIN_SIZE[0]):
                self.surface.blit(self.backImg, (x + self.xOffset,y))
                self.surface.blit(self.foreImg, (x + self.xOffset, 0))
        if not self.stopped:
            self.xOffset = (self.xOffset - (config['PX_STEP'] * multiplier)) % TERRAIN_SIZE[0]