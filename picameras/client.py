import socket
import time
from imutils.video import VideoStream
import imagezmq
import cv2
import json

with open('config.json') as config_file:
	config = json.load(config_file)

sender = imagezmq.ImageSender(connect_to='tcp://' + config['serverIp'])

hostname = socket.gethostname()
cam = VideoStream(src=-1, resolution=tuple(config['resolution']), framerate=config['framerate']).start()
time.sleep(3.0)

while True:
        image = cam.read()
        sender.send_image(hostname, image)