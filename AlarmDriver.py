from Configuration import Configuration
from Alarm import Alarm
from datetime import datetime
from time import sleep
def main():
    config = Configuration()
    while(1):
        alarm = Alarm(config)
        while datetime.now() < alarm.alarm_time:
            sleep(5) # drastically reduces CPU time while polling
        alarm.start_alarm()

main()
