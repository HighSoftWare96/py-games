from random import randrange
from threading import Timer

class Timeout():
    def __init__(self, min, max, task):
        self.min = min
        self.max = max
        self.task = task
        self.step()

    def step(self):
        self.task()
        self.timer = Timer(randrange(self.min, self.max) / 1000, self.step)
        self.timer.start()
        
timers = []

def createTimeout(min, max, task):
    timers.append(Timeout(min, max, task))

def stopAll():
    for t in timers:
        t.timer.cancel()