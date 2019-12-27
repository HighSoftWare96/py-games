from controllers.GameState import state
from pygame.font import Font
from helpers.config import config
import os
from definitions import ROOT_DIR

scoreColor = (255, 255,255)


class Score():
    def __init__(self):
        fullfontpath = os.path.join(ROOT_DIR, 'assets/fonts/coolvetica.ttf')
        self.font = Font(fullfontpath, 32)

    def update(self):
        self.text = self.font.render(str(state.score), True, scoreColor)
        self.rect = self.text.get_rect()
        self.rect.bottomright = (config['SCREEN_SIZE'][0] - 30, 50)

    def draw(self,screen):
        screen.blit(self.text, self.rect)