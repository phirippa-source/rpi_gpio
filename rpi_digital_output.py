import RPi.GPIO as GPIO
import time

pin_led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

for i in range(10):
    GPIO.output(pin_led, 0)
    time.sleep(1)
    GPIO.output(pin_led, 1)
    time.sleep(1)

#GPIO.cleanup()
