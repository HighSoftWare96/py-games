from sprites.Tree import Tree
from random import randrange
from threading import Timer
from pygame.sprite import Group

class TreeManager(Group):
    def __init__(self):
        Group.__init__(self)
        self._createTree()

    def _generateRandomTimeOffset(self):
        return randrange(800, 6000)

    def update(self, multiplier = 1):
        super().update(multiplier)
        for sprite in self:
            if sprite.isOffscreen():
                print('removed tree')
                self.remove(sprite)
    
    def _createTree(self):
        self.add(Tree())
        return Timer(self._generateRandomTimeOffset() / 1000, self._createTree).start()