# Import Files
from TakePicture import TakePicture
print('Imported Picture Taking')
from CloudsightAPI import UploadPicture
from CloudsightAPI import InitilizeCloudsight
import picamera
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
print('Imported Sound Playing')

#Functions Available:
#TakePicture()
#InitilizeCloudsight()
#UploadPicture()
#ErrorNetwork()
#Welcome()
#SpeakWord(WORD)
SpeakWord("Christmas Tree")
