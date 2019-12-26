#!/usr/bin/env python
import os, pygame
from pygame.locals import *
from pygame.sprite import collide_mask
from helpers.config import config
from helpers.game_state import GameState
from helpers.loaders import load_image, load_sound
from helpers.colors import RED, BLACK, WHITE
from managers.TreeManager import TreeManager
from sprites.Terrain import Terrain 
from sprites.Background import Background
from sprites.Santa import Santa
from controllers.GameState import state, RUNNING_STATE
from managers.Score import Score

pygame.init()   
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])

background = Background()
treeManager = TreeManager()
santa = Santa()
terrain = Terrain()
score = Score()

clock = pygame.time.Clock()

def gameOver():
    santa.kill()
    terrain.stop()
    treeManager.stop()
    background.stop()
    state.setGameOver()

def detectCollision():
    for tree in treeManager:
        if collide_mask(santa, tree):
            return True
    return False

while(True):

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                santa.jump()

    if detectCollision():
        gameOver()

    if state.getState() == RUNNING_STATE:
        state.increaseScore()

    score.update()
    treeManager.update()
    santa.update()
    screen.blit(background.getSurf(), background.getCoords())
    screen.blit(terrain.getSurf(), terrain.getCoords())
    santa.draw(screen)
    score.draw(screen)
    treeManager.draw(screen)
    pygame.display.flip()
    clock.tick(config['FPS'])