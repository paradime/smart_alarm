from Configuration import Configuration
from Alarm import Alarm
def main():
    config = Configuration()
    while(1):
        alarm = Alarm(config)
        while datetime.now() < alarm.alarm_time:
            sleep(5) # drastically reduces CPU time while polling
        alarm.start_alarm()

main()
