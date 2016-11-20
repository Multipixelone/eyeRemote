import picamera

from LocalVariables import takepicture

GPIO.setmode(GPIO.BCM)
camera = picamera.PiCamera()
GPIO.setup(takepicture, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    camera.capture('image.jpg')
