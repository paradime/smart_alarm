from Configuration import Configuration
from Alarm import Alarm

# File to manually test the services without waiting for the alarm
def main():
    config = Configuration()
    alarm = Alarm(config)
    alarm.start_alarm()

main()
