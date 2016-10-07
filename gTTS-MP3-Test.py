# Load gTTS, which allows Text to Speech
from gtts import gTTS
# Load Mixer, for Playing the mp3 file
from pygame import mixer

tts = gTTS(text='Welcome to the Remote! Press the Button for Information of what you're looking at!', lang='en')
tts.save("Welcome.mp3")

mixer.init()
mixer.music.load('Welcome.mp3')
mixer.music.play()
