#!/usr/bin/env python
import os, pygame
from helpers.config import config
from helpers.game_state import GameState
from helpers.loaders import load_image, load_sound
from helpers.colors import RED, BLACK, WHITE
from sprites.Tree import Tree

pygame.init()
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
screen.blit(background, (0, 0))
pygame.display.flip()

tree = Tree()

allsprites = pygame.sprite.RenderPlain((tree))
clock = pygame.time.Clock()

while(True):
    clock.tick(60)
    tree.update()
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()