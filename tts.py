from pydub import AudioSegment
from pygame import mixer
from gtts import gTTS

class TTS:
    def __init__(self):
        mixer.init(frequency=24000)

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('test.mp3')
        return 'test.mp3'

    def convert(self, mp3):
        song = AudioSegment.from_mp3(mp3)
        song.export('test.wav', format='wav')
        return 'test.wav'

    def play(self, wav):
        mixer.music.load(wav)
        mixer.music.play()
