from Configuration import Configuration
from Alarm import Alarm
def main():
    config = Configuration()
    alarm = Alarm(config)
    alarm.start_alarm()

main()
