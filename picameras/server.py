import cv2
import imagezmq
import json
import numpy as np
import signal
import sys
import imutils
from datetime import datetime

with open('server-config.json') as config_file:
    config = json.load(config_file)

image_hub = imagezmq.ImageHub()
# video_output_map = dict()

fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
writer = None
(h, w) = (None, None)
zeros = None


def on_end(sig, frame):
    print('You pressed Ctrl+C! Terminating streams...')
    cv2.destroyAllWindows()
    writer.release()
    sys.exit(0)


signal.signal(signal.SIGINT, on_end)
print('Press Ctrl+C to terminate recording!')

while True:
    cameraname, frame = image_hub.recv_image()
    frame = imutils.resize(frame, width=300)
    if writer is None:
        # store the image dimensions, initialize the video writer,
        # and construct the zeros array
        (h, w) = frame.shape[:2]
        writer = cv2.VideoWriter('test.mp4', fourcc, 20, (w, h), True)
        zeros = np.zeros((h, w), dtype="uint8")
    output = np.zeros((h, w, 3), dtype="uint8")
    output[0:h, 0:w] = frame
    writer.write(frame)
    cv2.imshow(cameraname, frame)
    key = cv2.waitKey(1) & 0xFF
    # video_output_map[cameraname].write(image)
    image_hub.send_reply(b'OK')
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            break

on_end()
