config_file = "secret_config.json"
from Configuration import Configuration
from Calendar import Calendar
from Weather import Weather
from datetime import datetime
from TTS import TTS
from QOTD import QOTD
from time import sleep
import json
class Alarm:
    def __init__(self, config):
        alarm_string = config.alarm["alarmtime"]
        self.config = config
        self.services = [Weather, Calendar, QOTD]
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
        self.play_text(self.config.alarm['greeting'])
        for service in self.services:
            try:
                text = service().get_info()
            except:
                text = 'There was en error connecting to the ' + service.__name__ + ' service'
            self.play_text(text)
        self.play_music()

    def play_text(self, text):
        tts = TTS()
        mp3 = tts.text_to_speech(text)
        wav = tts.convert(mp3)
        tts.play(wav)

    def play_music(self):
        tts = TTS(44100)
        wav = self.config.music['file']
        tts.play(wav)

