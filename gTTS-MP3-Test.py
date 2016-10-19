# Load gTTS, which allows Text to Speech
from gtts import gTTS
# Load Mixer, for Playing the mp3 file
import pygame

tts = gTTS(text='Welcome to the Remote! Press the Button for Information of what your looking at!', lang='en')
tts.save("Welcome.mp3")

pygame.mixer.init()
pygame.mixer.music.load('Welcome.mp3')
pygame.mixer.music.play()
