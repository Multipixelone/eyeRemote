import RPi.GPIO as GPIO
import os
from LocalVariables import shutdownpin
import PlaySounds
from PlaySounds import SpeakWord

GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdownpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(shutdownpin, GPIO.FALLING)
    SpeakWord("Shutting Down")
    print("Shutting down...")
    os.system("sudo shutdown now")
except:
    pass

GPIO.cleanup()
