import cv2
import json
import numpy as np
import signal
import sys
import os
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
import imutils
from datetime import datetime
from config import config
from imagehubadapter import imagehubadapter

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writers = dict()
(h, w) = (None, None)
zeros = None


def on_end(sig, frame):
    print('You pressed Ctrl+C! Terminating streams...')
    cv2.destroyAllWindows()
    for key in writers.keys():
        writers[key].release()
    sys.exit(0)


signal.signal(signal.SIGINT, on_end)
print('Press Ctrl+C to terminate recording!')

while True:
    cameraname, frame = imagehubadapter.readFrame()
    (h, w) = frame.shape[:2]
    filename = config['path'] + '/' + cameraname + datetime.now().strftime("%d_%m_%Y-%H:%M:%S") + '.mp4'
    if not cameraname in writers:
        # store the image dimensions, initialize the video writer,
        # and construct the zeros array
        writers[cameraname] = cv2.VideoWriter(filename, fourcc, float(config['framerate']), (w, h), True)
        zeros = np.zeros((h, w), dtype="uint8")
    output = np.zeros((h, w, 3), dtype="uint8")
    output[0:h, 0:w] = frame
    writers[cameraname].write(frame)
    cv2.imshow(cameraname, frame)
    key = cv2.waitKey(1) & 0xFF
    # video_output_map[cameraname].write(image)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

on_end()
