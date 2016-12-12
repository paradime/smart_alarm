from Configuration import Configuration
from Alarm import Alarm
from datetime import datetime
from time import sleep

# The main driver for the alarm clock
# This file can be replaced with a web server in the future
def main():
    config = Configuration()
    while(1): # loop forever
        alarm = Alarm(config)
        while datetime.now() < alarm.alarm_time: # loop until the current time is after the alarm time
            sleep(5) # drastically reduces CPU time while polling
        alarm.start_alarm()

main()
