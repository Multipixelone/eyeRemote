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
import PlaySounds
print('Imported Sound Playing')

#TakePicture()
InitilizeCloudsight()
UploadPicture()
