config_file = "secret_config.json"
from Calendar import Calendar
from Weather import Weather
from datetime import datetime
from TTS import TTS
from QOTD import QOTD
from time import sleep
import json

class Alarm:

    # This will setup the Alarm clock and initialize what time to go off
    def __init__(self, config):
        alarm_string = config.alarm["alarmtime"]
        self.config = config
        self.services = [Weather, Calendar, QOTD] # Remove any services here that you don't want
        self.set_alarm(alarm_string)

    # This will setup the alarm time and allow it to be compared
    def set_alarm(self, alarm_string):
        currtime = datetime.now()
        self.alarm_time = datetime.strptime(alarm_string, '%I:%M%p')
        self.alarm_time = self.alarm_time.replace(currtime.year, currtime.month, currtime.day)

        # If this is being set on the same day, but after the alarm would go off
        if self.alarm_time < currtime:
            self.alarm_time = self.alarm_time.replace(
                self.alarm_time.year,
                self.alarm_time.month,
                self.alarm_time.day + 1, # just add a day
                self.alarm_time.hour,
                self.alarm_time.minute
            )
    
    # Play all of the services
    # 1) Greet the user
    # 2) Play all services
    # 3) Play music
    def start_alarm(self):
        self.play_text(self.config.alarm['greeting'])
        for service in self.services:
            try:
                text = service().get_info() # duck typing
            except: # This is used if a services is unavailable, it will notify the user
                text = 'There was en error connecting to the ' + service.__name__ + ' service'
            self.play_text(text)
        self.play_music()

    # A simple wrapper for accepting text and then playing it
    def play_text(self, text):
        tts = TTS()
        mp3 = tts.text_to_speech(text)
        wav = tts.convert(mp3)
        tts.play(wav)

    # The default music file requires a frequency of 44100, in the future, this should be dynamic
    def play_music(self):
        tts = TTS(44100)
        wav = self.config.music['file']
        tts.play(wav)

