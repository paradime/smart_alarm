from pydub import AudioSegment
from pygame import mixer
from gtts import gTTS

mixer.init(frequency=24000)

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('test.mp3')
    return 'test.mp3'

def convert(mp3):
    song = AudioSegment.from_mp3(mp3)
    song.export('test.wav', format='wav')
    return 'test.wav'

def play(wav):
    mixer.music.load(wav)
    mixer.music.play()

play(convert(text_to_speech('kaleb is the best')))

