config_file = "secret_config.json"
from Configuration import Configuration
from datetime import datetime
import json
class Alarm:

    def __init__(self, config):
        alarm_string = config.alarm["alarmtime"]
        self.set_alarm(alarm_string)

    def set_alarm(self, alarm_string):
        currtime = datetime.now()
        self.alarm_time = datetime.strptime(alarm_string, '%I:%M%p')
        self.alarm_time = self.alarm_time.replace(currtime.year, currtime.month, currtime.day)

        if self.alarm_time < currtime:
            self.alarm_time = self.alarm_time.replace(
                self.alarm_time.year,
                self.alarm_time.month,
                self.alarm_time.day + 1,
                self.alarm_time.hour,
                self.alarm_time.minute
            )
    
    def start_alarm():
        pass
def main():
    config = Configuration()
    alarm = Alarm(config)

    while datetime.now() < alarm.alarm_time:
        pass

    print("buzz buzz")


main()
