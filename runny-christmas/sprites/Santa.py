from pygame.sprite import Sprite, GroupSingle
from pygame.mask import from_surface
from helpers.loaders import load_image
from helpers.config import config
from math import floor
from controllers.SoundManager import soundManager

SPRITE_CONFIG = config['SPRITES']['SANTA']
# ogni quanti FPS muovere lo sprite
MOVE_EACH_FPS = 2
JUMP_STEP = 8
# n di FPS in cui al salto Santa deve rimanere in volo
JUMP_ON_AIR_FPS = 5
MAX_JUMP_OFFSET = config['SPRITES']['TREE']['SIZE'][1] + 40

runningImages = []
jumpingImages = []
santaKilled = []


def loadAssets():
    santaKilled.append(load_image('santa/Dead.png', SPRITE_CONFIG['SIZE']))
    for i in range(11):
        runningImages.append(
            load_image('santa/Run (' + str(i + 1) + ').png',
                SPRITE_CONFIG['SIZE'])
        )
    for i in range(15):
        jumpingImages.append(
            load_image('santa/Jump (' + str(i + 1) + ').png',
                SPRITE_CONFIG['SIZE']))


class Santa(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        loadAssets()
        self.stopped = True
        self.animationStep = 0
        self.animationSkipper = 0
        self.jumping = False
        self.jumpingY = 0
        self.keepOnAir = JUMP_ON_AIR_FPS
        self.killed = False
        self._animate()
        self._positionate()

    def jump(self):
        if not self.jumping and self.jumpingY <= 15 and not self.killed:
            # suono del salto
            soundManager.playJump()
            self.keepOnAir = JUMP_ON_AIR_FPS
            self.jumping = True

    def kill(self):
        if not self.killed:
            # suono del colpo
            soundManager.playHit()
            self.killed = True

    def start(self):
        self.stopped = False
    
    def stop(self):
        self.stopped = True

    def update(self, multiplier=1):
        self._animate()
        self._positionate()

    def _animate(self):
        if self.stopped:
            self.image, self.rect = runningImages[0]
            return
        # animazione morto
        if self.killed:
            self.image, self.rect = santaKilled[0]
        # animazione per il salto
        elif self.jumping == True or self.jumpingY >= 15:
            # faccio una proporzione tra quantita di salto e # di immagini
            # per il salto per capire a che immagine sono arrivato
            jumpStep = floor(((len(jumpingImages) - 1) *
                              self.jumpingY) / MAX_JUMP_OFFSET)
            self.image, self.rect = jumpingImages[jumpStep]
        else:
            # animazione per la corsa
            self.image, self.rect = runningImages[self.animationStep]
            self.animationSkipper = (self.animationSkipper + 1) % MOVE_EACH_FPS
            if self.animationSkipper == 0:
                self.animationStep = (
                    self.animationStep + 1) % len(runningImages)
        self.mask = from_surface(self.image)

    def _positionate(self):
        self.rect.bottomright = (
            130, config['GROUND_POSITION'] - self.jumpingY + 10)
        self._setJumpingOffset()

    def _setJumpingOffset(self):
        if self.jumping:
            self.jumpingY += JUMP_STEP
            if self.jumpingY >= MAX_JUMP_OFFSET:
                self.jumping = False
        elif self.jumpingY > 0:
            # se siamo a zero posso farlo tornare per terra
            if self.keepOnAir == 0:
                self.jumpingY -= JUMP_STEP
            else:
                self.keepOnAir -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
