from pydub import AudioSegment
from pygame import mixer
from gtts import gTTS
from time import sleep

# Text to speech wrapper and player
class TTS:
    # The default is 24000, because that is what the TTS library creates wavs at
    def __init__(self, frequency=24000):
        self.mixer = mixer
        self.mixer.init(frequency=frequency)

    # Taxes in text and creates an mp3, returns the name of the mp3
    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('test.mp3')
        return 'test.mp3'

    # Creates an wav file that is a duplicate of the mp3
    def convert(self, mp3):
        song = AudioSegment.from_mp3(mp3)
        song.export('test.wav', format='wav')
        return 'test.wav'

    # Plays an audio file
    def play(self, wav):
        self.mixer.music.load(wav)
        self.mixer.music.play()
        while(self.mixer.music.get_busy()):
            sleep(1) # reduces CPU usage while polling
        self.mixer.quit()
