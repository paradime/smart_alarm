from pydub import AudioSegment
from pygame import mixer
from gtts import gTTS

class TTS:
    def __init__(self, frequency=24000):
        self.mixer = mixer
        self.mixer.init(frequency=frequency)

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('test.mp3')
        return 'test.mp3'

    def convert(self, mp3):
        song = AudioSegment.from_mp3(mp3)
        song.export('test.wav', format='wav')
        return 'test.wav'

    def play(self, wav):
        self.mixer.music.load(wav)
        self.mixer.music.play()
        while(self.mixer.music.get_busy()):
            pass
        self.mixer.quit()
