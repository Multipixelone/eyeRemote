import RPi.GPIO as GPIO
import os
from LocalVariables import shutdownpin
import PlaySounds
from PlaySounds import Shutdown

GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdownpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(shutdownpin, GPIO.FALLING)
    Shutdown()
    print("Shutting down...")
    os.system("sudo shutdown now")
except:
    pass

GPIO.cleanup()
