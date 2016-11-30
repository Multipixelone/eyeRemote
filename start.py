# Import Files
from TakePicture import TakePicture
print('Imported Picture Taking')
import CloudsightAPI
from CloudsightAPI import UploadPicture
#from CloudsightAPI import InitilizeCloudsight
import picamera
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
print('Imported Sound Playing')
from time import sleep
print('Imported Sleeping')

Welcome()
#Functions Available:
#TakePicture()
UploadPicture()
#from LocalVariables import LastScan
from CloudsightAPI import item
#ErrorNetwork()
#Welcome()
#SpeakWord(WORD)
SpeakWord(item)
