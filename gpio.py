from gpiozero import Button #import button library
import pygame #import pygame library
import RPi.GPIO as GPIO #import GPIO library
import time #import time library
import os #import os library
import sounddevice as sd
import wavio as wv

pygame.init() #initialize pygame

#set each sound as a variable that can be referenced
octive3 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Db3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/D3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Eb3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/E3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/F3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Gb3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/G3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Ab3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/A3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Bb3.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/B3.wav"]

octive4 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Db4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/D4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Eb4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/E4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/F4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Gb4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/G4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Ab4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/A4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Bb4.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/B4.wav"]

octive5 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Db5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/D5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Eb5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/E5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/F5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Gb5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/G5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Ab5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/A5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/Bb5.wav",
           "/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/B5.wav"]

custom = ["/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom1.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom2.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom3.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom4.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom5.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom6.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom7.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom8.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom9.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom10.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom11.wav",
          "/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom12.wav"]

btnPressed = [True, True, True, True, True, True, True, True, True, True, True, True]
pin=[12,20,16,26,19,13,6,12,0,7,8,11]
GPIO.setmode(GPIO.BCM)
for i in range(0, 12)
    GPIO.setup(pin[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

swch_pos1 = (9)
swch_pos3 = (10)

btn_mode = (23)
btn_rec = (24)

freq = 44100
duration = 5
update = True


GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def record(fileNo):
    print("Now recording...")
    recording = sd.rec(int(duration*freq), samplerate = freq, channels=2)
    sd.wait()
    print("Done recording...")
    wv.write("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom%d.wav" %fileNo, recording, freq, sampwidth = 2)
    #os.system("arecord /home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom%d.wav -D plughw:CARD=1 -f cd -d 5 &" %fileNo)

def clearCustom():
    custom1 = None
    custom2 = None
    custom3 = None
    custom4 = None
    custom5 = None
    custom6 = None
    custom7 = None
    custom8 = None
    custom9 = None
    custom10 = None
    custom11 = None
    custom12 = None
    update = True

def setupCustom():
    custom1 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom1.wav")
    custom2 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom2.wav")
    custom3 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom3.wav")
    custom4 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom4.wav")
    custom5 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom5.wav")
    custom6 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom6.wav")
    custom7 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom7.wav")
    custom8 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom8.wav")
    custom9 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom9.wav")
    custom10 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom10.wav")
    custom11 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom11.wav")
    custom12 = pygame.mixer.Sound("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom12.wav")
    update = False

print("switch pos1: " + str(GPIO.input(swch_pos1)))
print("switch pos3: " + str(GPIO.input(swch_pos3)))
print("Mode Btn: " + str(GPIO.input(btn_mode)))
print("Record Btn: " + str(GPIO.input(btn_rec)))

while 1:
    if GPIO.input(swch_pos1) == 0 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 1
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        for i in range(0,12):
            btnPressed[i] = GPIO.input(pin[i])
            if btnPressed[i] == False:
                pygame.mixer.Sound(octave3[i]).play                
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 2
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        for i in range(0,12):
            btnPressed[i] = GPIO.input(pin[i])
            if btnPressed[i] == False:
                pygame.mixer.Sound(octave4[i]).play 
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 0 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 3
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        for i in range(0,12):
            btnPressed[i] = GPIO.input(pin[i])
            if btnPressed[i] == False:
                pygame.mixer.Sound(octave5[i]).play         
    if GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 0:
        print("Mode Btn: " + str(GPIO.input(btn_mode)))
        print("Record Btn: " + str(GPIO.input(btn_rec)))
        time.sleep(0.15)
        for i in range(0,12):
            btnPressed[i] = GPIO.input(pin[i])
            if btnPressed[i] == False:
                record(i+1) #filenames are index+1            
    elif GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 1:
        if update:
            setupCustom()
        print("Mode Btn: " + str(GPIO.input(btn_mode)))
        print("Record Btn: " + str(GPIO.input(btn_rec)))
        time.sleep(0.15)
        for i in range(0,12):
            btnPressed[i] = GPIO.input(pin[i])
            if btnPressed[i] == False:
                pygame.mixer.Sound(custom[i]).play 
        
