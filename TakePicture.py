import picamera
import RPi.GPIO as GPIO

from LocalVariables import takepicture

GPIO.setmode(GPIO.BCM)
camera = picamera.PiCamera()
GPIO.setup(takepicture, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(takepicture)):
        camera.capture('image.jpg')
        print('PICTURE TAKEN :D')
