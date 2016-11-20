import RPi.GPIO as GPIO
import os
from LocalVariables import shutdownpin

GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdownpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    os.system("sudo shutdown -h now")
except:
    pass

GPIO.cleanup()
