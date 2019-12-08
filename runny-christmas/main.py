#!/usr/bin/env python
import os, pygame
from helpers.config import config
from helpers.game_state import GameState
from helpers.loaders import load_image, load_sound
from helpers.colors import RED, BLACK, WHITE
from sprites.Tree import Tree
from sprites.Terrain import Terrain 
from sprites.Background import Background

pygame.init()
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])


background = Background()
tree = Tree()
terrain = Terrain()

allsprites = pygame.sprite.RenderPlain((tree))
clock = pygame.time.Clock()

while(True):
    clock.tick(60)
    tree.update()
    screen.blit(background.getSurf(), background.getCoords())
    screen.blit(terrain.getSurf(), terrain.getCoords())
    allsprites.draw(screen)
    pygame.display.flip()