import pygame #import pygame library
import RPi.GPIO as GPIO #import GPIO library
import time #import time library
import sounddevice as sd #import sounddevice library
import wavio as wv #import wavio library

pygame.init() #initialize pygame

#set each sound as a variable that can be referenced
octave3 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C3.wav",
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

octave4 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C4.wav",
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

octave5 = ["/home/alex/Desktop/github/capstone/gpio-music-box/piano-mp3/C5.wav",
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

btnPressed = [True, True, True, True, True, True, True, True, True, True, True, True] #Set button pressed as a boolean set to true for each button
pin=[21,20,16,26,19,13,6,12,0,7,8,11] #Set the pins for each button
GPIO.setmode(GPIO.BCM) #Set the code to read the pin numbering
for i in range(0, 12): #Set the range of buttons from 0-12
    GPIO.setup(pin[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set the button pins as pull up, activated upon pull down
#Set the 3 position switch pins
swch_pos1 = (9) 
swch_pos3 = (10)
#Set the mode and record button pins
btn_mode = (23)
btn_rec = (24)
#Set the mode and record LED pins
mode_LED = (18) 
rec_LED = (22)
#Set frequency, duration, and update boolean
freq = 44100
duration = 5
update = True

#Set  3 position switch pins as pull up, activated upon pull down
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Set mode and record button pins as pull up, activated upon pull down
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Set mode and record LED pins as outputs
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def record(fileNo): #Define the parameters of the recording
    print("Now recording...")
    recording = sd.rec(int(duration*freq), samplerate = freq, channels=2)
    sd.wait()
    print("Done recording...")
    wv.write("/home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom%d.wav" %fileNo, recording, freq, sampwidth = 2)
    #os.system("arecord /home/alex/Desktop/github/capstone/gpio-music-box/CustomSounds/custom%d.wav -D plughw:CARD=1 -f cd -d 5 &" %fileNo)
#Turn off LEDs upon startup
GPIO.output(18,0)
GPIO.output(22,0)
#Show value of each pin (0 is active, 1 is inactive)
print("switch pos1: " + str(GPIO.input(swch_pos1)))
print("switch pos3: " + str(GPIO.input(swch_pos3)))
print("Mode Btn: " + str(GPIO.input(btn_mode)))
print("Record Btn: " + str(GPIO.input(btn_rec)))

while 1:
    if GPIO.input(swch_pos1) == 0 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1:#Check that position switch is in position 1
        GPIO.output(18,0) #Turn off LED
        GPIO.output(22,0) #Turn off LED
        print("switch pos1: " + str(GPIO.input(swch_pos1))) #print position 1 value
        print("switch pos3: " + str(GPIO.input(swch_pos3))) #print position 3 value
        time.sleep(0.15) #150ms delay
        for i in range(0,12): #Set the range of buttons from 0-12
            btnPressed[i] = GPIO.input(pin[i]) #Set btnPressed boolean based on value of pressed button (0 = active, 1 = inactive)
            if btnPressed[i] == False: #Check if button is pressed
                pygame.mixer.Sound(octave3[i]).play() #play certain sound based on button pressed               
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 2
        GPIO.output(18,0) #Turn off LED
        GPIO.output(22,0) #Turn off LED
        print("switch pos1: " + str(GPIO.input(swch_pos1))) #print position 1 value
        print("switch pos3: " + str(GPIO.input(swch_pos3))) #print position 3 value
        time.sleep(0.15) #150ms delay
        for i in range(0,12): #Set the range of buttons from 0-12
            btnPressed[i] = GPIO.input(pin[i]) #Set btnPressed boolean based on value of pressed button (0 = active, 1 = inactive)
            if btnPressed[i] == False:
                sound =pygame.mixer.Sound(octave4[i]).play() #play certain sound based on button pressed
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 0 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 3
        GPIO.output(18,0) #Turn off LED
        GPIO.output(22,0) #Turn off LED
        print("switch pos1: " + str(GPIO.input(swch_pos1))) #print position 1 value
        print("switch pos3: " + str(GPIO.input(swch_pos3))) #print position 3 value
        time.sleep(0.15) #150ms delay
        for i in range(0,12):  #Set the range of buttons from 0-12
            btnPressed[i] = GPIO.input(pin[i]) #Set btnPressed boolean based on value of pressed button (0 = active, 1 = inactive)
            if btnPressed[i] == False: #Set the range of buttons from 0-12
                pygame.mixer.Sound(octave5[i]).play() #play certain sound based on button pressed       
           
    if GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 0:
        GPIO.output(18,1) #Turn on LED
        GPIO.output(22,1) #Turn on LED
        print("Mode Btn: " + str(GPIO.input(btn_mode))) #print position of mode button (0 is active, 1 is inactive)
        print("Record Btn: " + str(GPIO.input(btn_rec))) #print position of record button (0 is active, 1 is inactive)
        time.sleep(0.15) #150ms delay
        for i in range(0,12): #Set the range of buttons from 0-12
            btnPressed[i] = GPIO.input(pin[i]) #Set btnPressed boolean based on value of pressed button (0 = active, 1 = inactive)
            if btnPressed[i] == False:
                record(i+1) #filenames are index+1, record sounds based of button pressed under the parameters of the record definition            
    elif GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 1:
        GPIO.output(18,1) #Turn on LED
        GPIO.output(22,0) #Turn off LED
        print("Mode Btn: " + str(GPIO.input(btn_mode))) #print position of mode button (0 is active, 1 is inactive)
        print("Record Btn: " + str(GPIO.input(btn_rec))) #print position of record button (0 is active, 1 is inactive)
        time.sleep(0.15) #150ms delay
        for i in range(0,12): #Set the range of buttons from 0-12
            btnPressed[i] = GPIO.input(pin[i]) #Set btnPressed boolean based on value of pressed button (0 = active, 1 = inactive
            if btnPressed[i] == False:
                pygame.mixer.Sound(custom[i]).play() #Play custom sound based on button pressed
