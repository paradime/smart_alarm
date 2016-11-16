config_file = "example_config.json"
from Configuration import Configuration
from datetime import datetime
import json
class Alarm:

    def __init__(self, config):
        self.is_on = False
        alarm_string = config.alarm["alarmtime"]
        self.alarm_time = datetime.strptime(alarm_string, '%I:%M%p')

    def set_alarm(new_time):
        self.alarm_time = new_time
    

    def turn_off():
        self.is_on = False


    def start_alarm():
        self.is_on = True


def main():
    config = Configuration()
    alarm = Alarm(config)

main()
