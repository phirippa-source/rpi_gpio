import RPi.GPIO as GPIO
import time

pin_btn = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if GPIO.input(pin_btn) == GPIO.HIGH:
    print('Btn pressed')
  time.sleep(0.1)
