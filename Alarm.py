config_file = "secret_config.json"
from Configuration import Configuration
from Calendar import Calendar
from Weather import Weather
from datetime import datetime
from TTS import TTS
from time import sleep
import json
class Alarm:

    def __init__(self, config):
        alarm_string = config.alarm["alarmtime"]
        self.services = [Weather, Calendar]
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
    
    def start_alarm(self):
        for service in self.services:
            self.play_text(service().get_info())
        self.play_music()

    def play_text(self, text):
        tts = TTS()
        mp3 = tts.text_to_speech(text)
        wav = tts.convert(mp3)
        tts.play(wav)

    def play_music(self):
        tts = TTS(44100)
        wav = tts.convert('jungle_falls.mp3')
        tts.play(wav)

def main():
    config = Configuration()
    alarm = Alarm(config)

    #while datetime.now() < alarm.alarm_time:
    alarm.start_alarm()
    print("buzz buzz")


main()
