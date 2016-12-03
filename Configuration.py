import json

class Configuration:

    def __init__(self):
        config_file = 'secret_config.json'
        with open(config_file) as data_file:
            data = json.load(data_file)
        
        self.weather = data["weather"]
        self.alarm = data["alarm"]
        self.music = data['music']

