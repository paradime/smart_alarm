config_file = "secret_config.json"
from Configuration import Configuration
from datetime import datetime
import json
class Alarm:

    def __init__(self, config):
        alarm_string = config.alarm["alarmtime"]
        self.alarm_time = datetime.strptime(alarm_string, '%I:%M%p')

    def set_alarm(new_time):
        self.alarm_time = new_time
    
    def start_alarm():
        pass

def main():
    config = Configuration()
    alarm = Alarm(config)

main()
