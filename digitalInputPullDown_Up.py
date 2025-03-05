import RPi.GPIO as GPIO
import time

pinSw = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if GPIO.input(pinSw) == GPIO.HIGH:
    print('Switch pressed')
  time.sleep(0.1)
