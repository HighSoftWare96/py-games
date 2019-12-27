from controllers.GameState import state
from pygame.font import Font
from pygame.surface import Surface
from pygame.locals import *
from helpers.config import config
import os
from definitions import ROOT_DIR
from controllers.GameState import state, RUNNING_STATE


FADE_IN_STEP = .5

scoreColor = (255, 0, 0)


class SplashScreen():
    def __init__(self):
        fullfontpath = os.path.join(ROOT_DIR, 'assets/fonts/wintersoul.ttf')
        self.h1Font = Font(fullfontpath, 50)
        self.fadeInValue = 255

    def pause(self):
        self.fadeInValue = 255

    def update(self):
        self.text = self.h1Font.render('RUNNY CHRISTMAS', True, scoreColor)
        self.rect = self.text.get_rect()
        self.rect.center = tuple([i / 2 for i in config['SCREEN_SIZE']])
        alpha_surf = Surface(self.text.get_size(), SRCALPHA)
        # Don't modify the original text surf.
        self.textWithAlpha = self.text.copy()
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, self.fadeInValue))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        self.textWithAlpha.blit(
            alpha_surf, (0, 0), special_flags=BLEND_RGBA_MULT)
        if state.state == RUNNING_STATE:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            self.fadeInValue = max(self.fadeInValue-FADE_IN_STEP, 0)

    def draw(self, screen):
        screen.blit(self.textWithAlpha, self.rect)
