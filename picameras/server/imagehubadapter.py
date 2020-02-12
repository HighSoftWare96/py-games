import imagezmq
from shared.config import config
import imutils

class _ImageHubAdapter:
    def __init__(self):
        self._hub = imagezmq.ImageHub()
    
    def readFrame(self):
        cameraname, frame = self._hub.recv_image()
        frame = imutils.resize(frame, width=int(config['resolution'][0]), height=int(config['resolution'][1]))
        self._hub.send_reply(b'OK')
        return (cameraname, frame)

imagehubadapter = _ImageHubAdapter()