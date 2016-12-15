from Configuration import Configuration
from Alarm import Alarm
from datetime import datetime
from multiprocessing import Process, Queue
from time import sleep
import os

class AlarmController:
    def __init__(self):
        self.processes = []
        self.alarm = self.get_alarm()

    def loop(self):
        while(1):
            self.alarm = self.get_alarm()
            while datetime.now() < self.alarm.alarm_time:
                sleep(5)
            self.start()

    def start(self):
        p = Process(target=self.alarm.start_alarm)
        p.start()
        self.processes.append(p)
        return 'start'

    def stop(self):
        if not self.processes.empty():
            self.processes.pop().terminate()
            return 'stop'
        else:
            return 'no processes to stop'

    def get_alarm(self):
        config = Configuration()
        return Alarm(config)
