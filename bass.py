from pygame import mixer
import time

mixer.init()
mixer.music.load('Seinfeld Theme - Bass.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.sleep(1)