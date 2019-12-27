#!/usr/bin/env python
import os, pygame, sys
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
from controllers.GameState import state, RUNNING_STATE, PAUSE_STATE
from managers.Score import Score
from controllers.SoundManager import soundManager
from helpers.timers import stopAll
from managers.SplashScreen import SplashScreen

pygame.init()   
screen = pygame.display.set_mode(config['SCREEN_SIZE'])
pygame.display.set_caption(config['SCREEN_TITLE'])

background = Background()
treeManager = TreeManager()
santa = Santa()
terrain = Terrain()
score = Score()
splash = SplashScreen()

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

def startAll():
    background.start()
    treeManager.start()
    santa.start()
    terrain.start()
    state.start()


def pauseAll():
    background.stop()
    treeManager.stop()
    santa.stop()
    terrain.stop()
    state.pause()
    splash.pause()

running = True
startAll()

while(running):

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                santa.jump()
            if event.key == K_ESCAPE:
                if state.state == RUNNING_STATE:
                    pauseAll()
                elif state.state == PAUSE_STATE:
                    startAll()

    if detectCollision():
        gameOver()

    if state.getState() == RUNNING_STATE:
        state.increaseScore()

    splash.update()
    score.update()
    treeManager.update()
    santa.update()
    screen.blit(background.getSurf(), background.getCoords())
    screen.blit(terrain.getSurf(), terrain.getCoords())
    santa.draw(screen)
    score.draw(screen)
    splash.draw(screen)
    treeManager.draw(screen)
    pygame.display.flip()
    clock.tick(config['FPS'])

# out of infinite loop
stopAll()
pygame.display.quit()
pygame.quit()
sys.exit(0)