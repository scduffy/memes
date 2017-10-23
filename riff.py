from pygame import *
import RPi.GPIO as GPIO
import time

# mixer.init()
# mixer.music.load('Seinfeld Theme - Bass.mp3')
# mixer.music.play()
#
# while mixer.music.get_busy():
#     time.Clock().tick(10)

while True:
    pin = 10
    GPIO.setup(pin, GPIO.IN)
    state = GPIO.input(pin)
    if state is True:
        mixer.init()
        mixer.music.load('Seinfeld Theme - Bass.mp3')
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(1)
    else:
        time.sleep(1)
