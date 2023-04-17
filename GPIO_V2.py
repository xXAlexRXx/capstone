#import libraries
from playsound import playsound
import sounddevice as sd
import RPi.GPIO as GPIO
import wavio as wv
import time

#Set each buttons pin value
GPIO.setmode(GPIO.BCM)
btn_C = (21)
btn_Db = (20)
btn_D = (16)
btn_Eb = (26)
btn_E = (19)
btn_F = (13)
btn_Gb = (6)
btn_G = (12)
btn_Ab = (0)
btn_A = (7)
btn_Bb = (8)
btn_B = (11)

swch_pos1 = (9)
swch_pos3 = (10)

btn_mode = (23)
btn_rec = (24)

#Set each button as pull-up, activated when pulled low (0)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

freq = 44100
duration = 3

def recording ()


while(1):
  if GPIO.input(swch_pos1) == 0 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1:
    if GPIO.input(btn_C) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/C3.wav")
    if GPIO.input(btn_Db) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Db3.wav")
    if GPIO.input(btn_D) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/D3.wav")
    if GPIO.input(btn_Eb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Eb3.wav")
    if GPIO.input(btn_E) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/E3.wav")
    if GPIO.input(btn_F) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/F3.wav")
    if GPIO.input(btn_Gb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Gb3.wav")
    if GPIO.input(btn_G) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/G3.wav")
    if GPIO.input(btn_Ab) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Ab3.wav")
    if GPIO.input(btn_A) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/A3.wav")
    if GPIO.input(btn_Bb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Bb3.wav")
    if GPIO.input(btn_B) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/B3.wav")
  elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1:
    if GPIO.input(btn_C) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/C4.wav")
    if GPIO.input(btn_Db) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Db4.wav")
    if GPIO.input(btn_D) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/D4.wav")
    if GPIO.input(btn_Eb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Eb4.wav")
    if GPIO.input(btn_E) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/E4.wav")
    if GPIO.input(btn_F) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/F4.wav")
    if GPIO.input(btn_Gb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Gb4.wav")
    if GPIO.input(btn_G) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/G4.wav")
    if GPIO.input(btn_Ab) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Ab4.wav")
    if GPIO.input(btn_A) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/A4.wav")
    if GPIO.input(btn_Bb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Bb4.wav")
    if GPIO.input(btn_B) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/B4.wav")
  elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 0:
    if GPIO.input(btn_C) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/C5.wav")
    if GPIO.input(btn_Db) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Db5.wav")
    if GPIO.input(btn_D) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/D5.wav")
    if GPIO.input(btn_Eb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Eb5.wav")
    if GPIO.input(btn_E) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/E5.wav")
    if GPIO.input(btn_F) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/F5.wav")
    if GPIO.input(btn_Gb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Gb5.wav")
    if GPIO.input(btn_G) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/G5.wav")
    if GPIO.input(btn_Ab) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Ab5.wav")
    if GPIO.input(btn_A) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/A5.wav")
    if GPIO.input(btn_Bb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Bb5.wav")
    if GPIO.input(btn_B) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/B5.wav")
      
  if GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 1:
    if GPIO.input(btn_C) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom1.wav")
    if GPIO.input(btn_Db) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom2.wav")
    if GPIO.input(btn_D) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom3.wav")
    if GPIO.input(btn_Eb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom4.wav")
    if GPIO.input(btn_E) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom5.wav")
    if GPIO.input(btn_F) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom6.wav")
    if GPIO.input(btn_Gb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom7.wav")
    if GPIO.input(btn_G) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom8.wav")
    if GPIO.input(btn_Ab) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom9.wav")
    if GPIO.input(btn_A) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom10.wav")
    if GPIO.input(btn_Bb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom11.wav")
    if GPIO.input(btn_B) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom12.wav")
  elif GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 0:
    if GPIO.input(btn_C) == 0:
      wv.write("/home/pi/gpio-music-box/piano-mp3/Custom1.wav", recording, freq, sampwidth = 2)
    if GPIO.input(btn_Db) == 0:
      wv.write("/home/pi/gpio-music-box/piano-mp3/Custom2.wav")
    if GPIO.input(btn_D) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom3.wav")
    if GPIO.input(btn_Eb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom4.wav")
    if GPIO.input(btn_E) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom5.wav")
    if GPIO.input(btn_F) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom6.wav")
    if GPIO.input(btn_Gb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom7.wav")
    if GPIO.input(btn_G) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom8.wav")
    if GPIO.input(btn_Ab) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom9.wav")
    if GPIO.input(btn_A) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom10.wav")
    if GPIO.input(btn_Bb) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom11.wav")
    if GPIO.input(btn_B) == 0:
      playsound("/home/pi/gpio-music-box/piano-mp3/Custom12.wav")
