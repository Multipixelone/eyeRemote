## Import Files
print('eyeRemote by Multipixelone on Github.')
from TakePicture import TakePicture
from LocalVariables import takepicture
print('Imported Picture Taking')
from Cloudsight import UploadPicture
from cloudsight import errors
import cloudsight
import requests
print('Imported Image Uploading')
import RPi.GPIO as GPIO
print('Imported GPIO')
from PlaySounds import Welcome
from PlaySounds import ErrorNetwork
from PlaySounds import SpeakWord
from PlaySounds import PictureTaken
print('Imported Sound Playing')
from time import sleep
print('Imported Sleeping')

## Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(takepicture, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

## Code to take picture:
#print('Waiting for inputs!')
#while True:
#  if (GPIO.input(takepicture)):
#    TakePicture()



## Actual code now: 
Welcome()
print('Waiting for inputs!')
while True:
  input_state = GPIO.input(takepicture)
  if input_state == False:
    TakePicture()
    PictureTaken()
    try:
         UploadPicture()
    except requests.ConnectionError:
         ErrorNetwork()
    except errors.APIError:
         SpeakWord("Invalid Cloudsight Key, please run install script")
    except KeyError:
         SpeakWord("Error Recognizing. Try something else") 
    else:
         from Cloudsight import item
         SpeakWord(item)

    
