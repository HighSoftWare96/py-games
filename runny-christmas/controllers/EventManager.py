import pygame
from pygame.locals import *

class EventManager():
    def handleEvent(self, eventQueue):
        for event in eventQueue:
            if event.type == KEYDOWN:
                self.handleKeyboard(event)

    def handleKeyboard(self), event:
        if event.key == K_SPACE:
            # todo: santa.jump!
