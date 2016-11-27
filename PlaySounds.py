from sultan.api import Sultan

s = Sultan()

def ErrorSounds():
	s.sudo("mpg123 Offline.mp3").run()
