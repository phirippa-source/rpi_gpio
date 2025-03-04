import RPi.GPIO as GPIO
import time

pin_btn = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def event_handler(channel):
  print(f'Btn(GPIO{channel}) Pressed')

GPIO.add_event_detect(pin_btn, GPIO.RISING, callback=event_handler)

while True:
  time.sleep(0.1)
