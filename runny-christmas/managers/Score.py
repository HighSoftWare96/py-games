from controllers.GameState import state
from pygame.font import Font
from helpers.config import config

red = (255, 0, 0)


class Score():
    def __init__(self):
        self.font = Font('freesansbold.ttf', 32)

    def update(self):
        self.text = self.font.render(str(state.score), True, red)
        self.rect = self.text.get_rect()
        self.rect.bottomright = (config['SCREEN_SIZE'][0] - 30, 50)

    def draw(self,screen):
        screen.blit(self.text, self.rect)