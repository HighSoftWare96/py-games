import os
import pygame
from pygame.locals import *
from pygame.transform import smoothscale
from definitions import ROOT_DIR

assets_dir = 'assets'
imageCache = {}


def load_image(name, size, opacity=1):
    print(os.path.join(ROOT_DIR, assets_dir, name))
    fullname = os.path.join(ROOT_DIR, assets_dir, name)
    uniqueKey = fullname + '#' + str(size) + '#' + str(opacity)

    # cerco se sono cachati da qualche parte
    if uniqueKey in imageCache:
        print('Cached')
        cachedImage = imageCache[uniqueKey].copy()
        return cachedImage, cachedImage.get_rect()

    # caricamento dell'immagine
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = image.convert_alpha()
    image = smoothscale(image, size)

    # salvo nella cache
    imageCache[uniqueKey] = image.copy()
    return image, image.get_rect()


def load_sound(name):
    fullname = os.path.join(ROOT_DIR, assets_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', message)
        raise SystemExit(message)
    return sound
