import RPi.GPIO as GPIO
import os
from LocalVariables import shutdownpin

GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdownpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    GPIO.wait_for_edge(shutdownpin, GPIO.FALLING)
    os.system("sudo shutdown now")

