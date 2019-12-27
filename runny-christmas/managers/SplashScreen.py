from controllers.GameState import state
from pygame.font import Font
from pygame.surface import Surface
from pygame.locals import *
from helpers.config import config
from helpers.loaders import load_image
import os
from definitions import ROOT_DIR
from controllers.GameState import state, PAUSE_STATE, RUNNING_STATE, GAMEOVER_STATE


FADE_IN_STEP = .5
CENTER_POSITION = tuple([i / 2 for i in config['SCREEN_SIZE']])

scoreColor = (255, 0, 0)
subColor = (255, 255, 255)


class SplashScreen():
    def __init__(self):
        fullfontpathH1 = os.path.join(ROOT_DIR, 'assets/fonts/wintersoul.ttf')
        fullfontpathH2 = os.path.join(ROOT_DIR, 'assets/fonts/coolvetica.ttf')
        self.h1Font = Font(fullfontpathH1, 50)
        self.h2Font = Font(fullfontpathH2, 24)
        self.fadeInValue = 255
        self.refreshImage, self.refreshImageRect = load_image('refresh.png', (30, 30))
        self.refreshImageRect.center = (config['SCREEN_SIZE'][0] - 20, config['SCREEN_SIZE'][1] - 20)

    def refreshClicked(self, pos):
        return self.refreshImageRect.collidepoint(pos)

    def pause(self):
        self.fadeInValue = 255

    def update(self):
        self._renderh1()
        # Valori vuoti per h2
        self.textH2 = None
        self.rectH2 = None
        if state.state == RUNNING_STATE:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            self.fadeInValue = max(self.fadeInValue-FADE_IN_STEP, 0)
        elif state.state == PAUSE_STATE:
            self.fadeInValue = 255
            self._renderPause()
        elif state.state == GAMEOVER_STATE:
            self.fadeInValue = 255
            self._renderGameover()

    def draw(self, screen):
        screen.blit(self.refreshImage, self.refreshImageRect)
        screen.blit(self.textWithAlpha, self.rect)
        if self.textH2:
            screen.blit(self.textH2, self.rectH2)

    def _renderh1(self):
        self.text = self.h1Font.render('RUNNY CHRISTMAS', True, scoreColor)
        self.rect = self.text.get_rect()
        self.rect.center = CENTER_POSITION
        alpha_surf = Surface(self.text.get_size(), SRCALPHA)
        # Don't modify the original text surf.
        self.textWithAlpha = self.text.copy()
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, self.fadeInValue))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        self.textWithAlpha.blit(
            alpha_surf, (0, 0), special_flags=BLEND_RGBA_MULT)

    def _renderPause(self):
        self.textH2 = self.h2Font.render('PAUSED', True, subColor)
        self.rectH2 = self.textH2.get_rect()
        self.rectH2.center = (CENTER_POSITION[0], CENTER_POSITION[1] + 40)

    def _renderGameover(self):
        self.textH2 = self.h2Font.render('GAME OVER!', True, subColor)
        self.rectH2 = self.textH2.get_rect()
        self.rectH2.center = (CENTER_POSITION[0], CENTER_POSITION[1] + 40)
