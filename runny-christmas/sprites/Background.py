from helpers.loaders import load_image
from helpers.config import config
from pygame import Surface
from helpers.colors import WHITE
from random import randrange
from threading import Timer
from helpers.timers import createTimeout

CHANGE_TIME_SKIPPER = 1000
SCREEN_SIZE = config['SCREEN_SIZE']
backgroundImages = []


class Background():
    def __init__(self):
        self.loadImages()
        self.stopped = True
        self.layer0, self.layer0_rect = backgroundImages[0]

        # cambia il tempo del gioco ogni tot FPS
        self.timeTracker = 0
        # 0 = mattina, 1 = pomeriggio, 2 = tramonto, 3 = notte
        self.timePhase = 0
        self.layer1, self.layer1_rect = load_image(
            'background1.png', SCREEN_SIZE, 0.8)
        self.layer1Offset = 0
        self.layer1Step = 3

        self.layer2, self.layer2_rect = load_image(
            'background2.png', SCREEN_SIZE, 0.3)
        self.layer2Offset = -35
        self.layer2Step = 1

        self.snowSize = (1198, 380)
        self.snow, self.snow_rect = load_image('snow.png', self.snowSize)
        self.snowOffset = 0
        self.snowStep = 4

        self.background = Surface(SCREEN_SIZE)
        self.background = self.background.convert()
        self.background.fill(WHITE)
        self._updateImages()

        # randomize snow time start
        createTimeout(800, 6000, self.randomizeSnow)

    def loadImages(self):
        for i in range(4):
            backgroundImages.append(load_image('background/' + str(i) + '.png',SCREEN_SIZE))

    def getSurf(self):
        self._updateImages()
        return self.background

    def getCoords(self):
        return (0, 0)

    def start(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def randomizeSnow(self):
        self.snowStep = randrange(3, 6)
        print(self.snowStep)

    def _updateImages(self):
        self.changeTime()
        self.background.blit(self.layer0, (0, 0))
        self.background.blit(self.snow, (0, self.snowOffset))
        self.background.blit(
            self.snow, (0,  self.snowOffset - self.snowSize[1]))
        self.snowOffset = (self.snowOffset + self.snowStep) % self.snowSize[1]
        self.background.blit(self.layer1, (0 - self.layer1Offset, 135))
        self.background.blit(
            self.layer1, (SCREEN_SIZE[0] - self.layer1Offset, 135))
        self.background.blit(self.layer2, (0 - self.layer2Offset, 135))
        self.background.blit(
            self.layer2, (SCREEN_SIZE[0] - self.layer2Offset, 135))
        if not self.stopped:
            self.layer1Offset = (self.layer1Offset +
                                 self.layer1Step) % SCREEN_SIZE[0]
            self.layer2Offset = (self.layer2Offset +
                                 self.layer2Step) % SCREEN_SIZE[0]

    def changeTime(self):
        if self.timeTracker == 0:
            self.layer0, self.layer0_rect = backgroundImages[self.timePhase]
            self.timePhase = (self.timePhase + 1) % 4
        self.timeTracker = (self.timeTracker + 1) % CHANGE_TIME_SKIPPER
