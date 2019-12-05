import os, pygame
from pygame.locals import *
from definitions import ROOT_DIR

assets_dir = 'assets'


def load_image(name):
    print(os.path.join(ROOT_DIR, assets_dir, name))
    fullname = os.path.join(ROOT_DIR, assets_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    return image, image.get_rect()


def load_sound(name):
    fullname = os.path.join(assets_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', wav)
        raise SystemExit(message)
    return sound