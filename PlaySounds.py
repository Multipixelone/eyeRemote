from sultan.api import Sultan

s = Sultan()

def ErrorNetwork():
	s.sudo("mpg123 Sounds/NetworkError.mp3").run()
def Welcome():
	s.sudo("mpg123 Sounds/Welcome.mp3").run()
