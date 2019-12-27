from sprites.Tree import Tree
from random import randrange
from helpers.timers import createTimeout
from pygame.sprite import Group


class TreeManager(Group):
    def __init__(self):
        Group.__init__(self)
        createTimeout(800, 6000, self._createTree)
        self.stopped = False

    def _generateRandomTimeOffset(self):
        return randrange(800, 6000)

    def stop(self):
        self.stopped = True

    def update(self, multiplier = 1):
        if self.stopped:
            return
        super().update(multiplier)
        for sprite in self:
            if sprite.isOffscreen():
                print('removed tree')
                self.remove(sprite)
    
    def _createTree(self):
        self.add(Tree())