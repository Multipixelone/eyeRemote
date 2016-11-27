# Import Files
print(' ')
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
print('Imported Sound Playing')

#TakePicture()
#InitilizeCloudsight()
#UploadPicture()
ErrorNetwork()
