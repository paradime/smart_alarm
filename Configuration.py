import json

class Configuration:

    # This just pulls information from the secret_config.json
    def __init__(self):
        config_file = 'secret_config.json'
        with open(config_file) as data_file:
            data = json.load(data_file)
        
        # create shortcuts for top level keys
        self.weather = data["weather"]
        self.alarm = data["alarm"]
        self.music = data['music']

