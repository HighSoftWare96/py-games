from controllers.SoundManager import soundManager

LOADING_STATE = -2
MENU_STATE = -1
PAUSE_STATE = 0
STARTED_STATE = 1
RUNNING_STATE = 2
GAMEOVER_STATE = 3

SCORE_SKIP_EACH = 10

class GameState():
    def __init__(self):
        self.state = LOADING_STATE
        self.score = 0
        self.scoreSkipper = 0

    def start(self, reset = False):
        if reset:
            self.score = 0
            self.scoreSkipper = 0
        self.state = RUNNING_STATE

    def pause(self):
        self.state = PAUSE_STATE

    def stop(self):
        self.state = None

    def increaseScore(self):
        if self.scoreSkipper == 0:
            self.score += 1
            if self.score % 100 == 0:
                soundManager.play100()
        self.scoreSkipper = (self.scoreSkipper + 1) % SCORE_SKIP_EACH

    def getState(self):
        return self.state
    
    def setStarted(self):
        self.state = STARTED_STATE
    
    def setGameOver(self):
        self.state = GAMEOVER_STATE

state = GameState()