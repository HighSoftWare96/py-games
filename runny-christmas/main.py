#!/usr/bin/env python
import os, pygame
from helpers.config import config
from helpers.game_state import GameState
from helpers.loaders import load_image, load_sound
from helpers.colors import RED, BLACK, WHITE
from managers.TreeManager import TreeManager
from sprites.Terrain import Terrain 
from sprites.Background import Background

pygame.init()
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])


background = Background()
treeManager = TreeManager()
terrain = Terrain()

clock = pygame.time.Clock()

while(True):
    pygame.event.get()
    treeManager.update()
    screen.blit(background.getSurf(), background.getCoords())
    screen.blit(terrain.getSurf(), terrain.getCoords())
    treeManager.draw(screen)
    pygame.display.flip()
    clock.tick(config['FPS'])