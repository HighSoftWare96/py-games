import json, os
from definitions import ROOT_DIR

config = None

fullpath = os.path.join(ROOT_DIR, 'config.json')
with open(fullpath) as jsonFile:
    config = json.load(jsonFile)