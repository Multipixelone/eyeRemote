## Import Files
from TakePicture import TakePicture
import picamera
print('Imported Picture Taking')
import CloudsightAPI
from CloudsightAPI import UploadPicture
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
print('Imported Sound Playing')
from time import sleep
print('Imported Sleeping')

## Functions Available:
#TakePicture()
#UploadPicture()
#ErrorNetwork()
#Welcome()
#SpeakWord(WORD)

## Code to upload image.jpg, return a json response, import that, and then speak it out
#UploadPicture()
#from CloudsightAPI import item
#SpeakWord(item)
