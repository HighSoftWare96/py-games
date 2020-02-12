import json
print(__file__)
with open('./server-config.json') as config_file:
    config = json.load(config_file)