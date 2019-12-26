#!/usr/bin/env python
import os, pygame
from pygame.locals import *
from helpers.config import config
from helpers.game_state import GameState
from helpers.loaders import load_image, load_sound
from helpers.colors import RED, BLACK, WHITE
from managers.TreeManager import TreeManager
from sprites.Terrain import Terrain 
from sprites.Background import Background
from sprites.Santa import getGroup, loadAssets

pygame.init()   
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])
loadAssets()


background = Background()
treeManager = TreeManager()
santa = getGroup()
terrain = Terrain()

clock = pygame.time.Clock()

while(True):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                santa.sprites()[0].jump()
    treeManager.update()
    santa.update()
    screen.blit(background.getSurf(), background.getCoords())
    screen.blit(terrain.getSurf(), terrain.getCoords())
    santa.draw(screen)
    treeManager.draw(screen)
    pygame.display.flip()
    clock.tick(config['FPS'])