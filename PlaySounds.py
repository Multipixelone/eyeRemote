from sultan.api import Sultan
from gtts import gTTS

s = Sultan()

def ErrorNetwork():
	s.sudo("mpg123 Sounds/NetworkError.mp3").run()
def Welcome():
	s.sudo("mpg123 Sounds/Welcome.mp3").run()
def SpeakWord( word ):
	tts = gTTS(text=word, lang='en')
	tts.save("Sounds/LastSpoken.mp3")
	s.sudo("mpg123 Sounds/LastSpoken.mp3").run()
def PictureTaken():
	s.sudo("mpg123 Sounds/Picture.mp3").run()
