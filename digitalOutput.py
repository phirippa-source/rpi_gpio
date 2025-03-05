import RPi.GPIO as GPIO
import time

pinLed = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)

for i in range(10):
    GPIO.output(pinLed, 0)
    time.sleep(1)
    GPIO.output(pinLed, 1)
    time.sleep(1)

GPIO.cleanup()
