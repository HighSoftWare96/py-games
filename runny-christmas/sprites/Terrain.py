from pygame.locals import *
from helpers.loaders import load_image
from helpers.config import config
from pygame import Surface
from random import randrange

TERRAIN_CONFIG = config['TERRAIN']
TERRAIN_SIZE = TERRAIN_CONFIG['SIZE']

class Terrain():
    def __init__(self):
        self.stopped = False
        self.surface = Surface((config['SCREEN_SIZE'][0], config['SCREEN_SIZE'][1] 
        - config['GROUND_POSITION']))
        self.surface = self.surface.convert()
        self.xOffset = 0
        self._loadImages()

    def getSurf(self):
        self._fillWithTextures()
        return self.surface

    def stop(self):
        self.stopped = True

    def getCoords(self):
        return (0,config['GROUND_POSITION'])

    def _loadImages(self):
        self.backImg, self.backImgRect = load_image('terrain.png',  TERRAIN_SIZE)
        self.foreImg, self.foreImgRect = load_image('terrain_fore.png', TERRAIN_SIZE) 


    def _fillWithTextures(self):
        if self.stopped:
            return
        totalXSpace = config['SCREEN_SIZE'][0] + (2 * TERRAIN_SIZE[0])
        for y in range(0, config['SCREEN_SIZE'][1], TERRAIN_SIZE[1]):
            for x in range(-TERRAIN_SIZE[0], totalXSpace, TERRAIN_SIZE[0]):
                self.surface.blit(self.backImg, (x + self.xOffset,y))
                self.surface.blit(self.foreImg, (x + self.xOffset, 0))
        self.xOffset = (self.xOffset - config['PX_STEP']) % TERRAIN_SIZE[0]