#!/usr/bin/python
import picamera
import RPi.GPIO as GPIO

from LocalVariables import takepicture

camera = picamera.PiCamera()

def TakePicture():
    camera.capture('image.jpg')
    print('Picture Taken')
