from pygame.mixer import Sound, music, init
from helpers.loaders import load_sound
import os
from definitions import ROOT_DIR

class SoundManager():
    def __init__(self):
        init()
        self.hitSound = load_sound('sounds/hit.wav')
        self.jumpSound = load_sound('sounds/jump.wav')
        self.soundEach100 = load_sound('sounds/100.wav')
        self.backSong = load_sound('songs/song1.ogg')
        self.backSong.play(loops = -1, fade_ms = 2400)
        self.backSong.set_volume(0.1)


    def playHit(self):
        Sound.play(self.hitSound)

    def playJump(self):
        Sound.play(self.jumpSound)

    def play100(self):
        Sound.play(self.soundEach100)
        

soundManager = SoundManager()