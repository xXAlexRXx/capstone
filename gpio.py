from gpiozero import Button #import button library
#from recorder import Recorder #import recorder library
import pygame #import pygame library
import RPi.GPIO as GPIO #import GPIO library
import time #import time library

pygame.init() #initialize pygame

#set each sound as a variable that can be referenced
C3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/C3.wav")
Db3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Db3.wav")
D3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/D3.wav")
Eb3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Eb3.wav")
E3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/E3.wav")
F3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/F3.wav")
Gb3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Gb3.wav")
G3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/G3.wav")
Ab3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Ab3.wav")
A3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/A3.wav")
Bb3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Bb3.wav")
B3 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/B3.wav")

C4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/C4.wav")
Db4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Db4.wav")
D4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/D4.wav")
Eb4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Eb4.wav")
E4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/E4.wav")
F4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/F4.wav")
Gb4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Gb4.wav")
G4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/G4.wav")
Ab4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Ab4.wav")
A4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/A4.wav")
Bb4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Bb4.wav")
B4 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/B4.wav")

C5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/C5.wav")
Db5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Db5.wav")
D5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/D5.wav")
Eb5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Eb5.wav")
E5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/E5.wav")
F5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/F5.wav")
Gb5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Gb5.wav")
G5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/G5.wav")
Ab5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Ab5.wav")
A5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/A5.wav")
Bb5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/Bb5.wav")
B5 = pygame.mixer.Sound("/home/pi/gpio-music-box/piano-mp3/B5.wav")

custom1 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom1.wav")
custom2 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom2.wav")
custom3 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom3.wav")
custom4 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom4.wav")
custom5 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom5.wav")
custom6 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom6.wav")
custom7 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom7.wav")
custom8 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom8.wav")
custom9 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom9.wav")
custom10 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom10.wav")
custom11 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom11.wav")
custom12 = pygame.mixer.Sound("/home/pi/gpio-music-box/CustomSounds/custom12.wav")



#set each button as a variable that can be referenced
GPIO.setmode(GPIO.BCM)
btn_C = Button(21)
btn_Db = Button(20)
btn_D = Button(16)
btn_Eb = Button(26)
btn_E = Button(19)
btn_F = Button(13)
btn_Gb = Button(6)
btn_G = Button(12)
btn_Ab = Button(0)
btn_A = Button(7)
btn_Bb = Button(8)
btn_B = Button(11)

swch_pos1 = (9)
swch_pos3 = (10)

btn_mode = (23)
btn_rec = (24)

#set the switches and buttons as inputs all high, activated when pulled low (circuit is connected)
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

print("switch pos1: " + str(GPIO.input(swch_pos1)))
print("switch pos3: " + str(GPIO.input(swch_pos3)))
print("Mode Btn: " + str(GPIO.input(btn_mode)))
print("Record Btn: " + str(GPIO.input(btn_rec)))

'''custom1 = Recorder()
custom2 = Recorder()
custom3 = Recorder()
custom4 = Recorder()
custom5 = Recorder()
custom6 = Recorder()
custom7 = Recorder()
custom8 = Recorder()
custom9 = Recorder()
custom10 = Recorder()
custom11 = Recorder()
custom12 = Recorder()'''

while 1:
    if GPIO.input(swch_pos1) == 0 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 1
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        btn_C.when_pressed = C3.play            
        btn_Db.when_pressed = Db3.play
        btn_D.when_pressed = D3.play
        btn_Eb.when_pressed = Eb3.play
        btn_E.when_pressed = E3.play
        btn_F.when_pressed = F3.play #Play 3rd octave notes
        btn_Gb.when_pressed = Gb3.play
        btn_G.when_pressed = G3.play
        btn_Ab.when_pressed = Ab3.play
        btn_A.when_pressed = A3.play
        btn_Bb.when_pressed = Bb3.play
        btn_B.when_pressed = B3.play
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 1 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 2
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        btn_C.when_pressed = C4.play
        btn_Db.when_pressed = Db4.play
        btn_D.when_pressed = D4.play
        btn_Eb.when_pressed = Eb4.play
        btn_E.when_pressed = E4.play
        btn_F.when_pressed = F4.play #Play 4th octave notes
        btn_Gb.when_pressed = Gb4.play
        btn_G.when_pressed = G4.play
        btn_Ab.when_pressed = Ab4.play
        btn_A.when_pressed = A4.play
        btn_Bb.when_pressed = Bb4.play
        btn_B.when_pressed = B4.play
    elif GPIO.input(swch_pos1) == 1 and GPIO.input(swch_pos3) == 0 and GPIO.input(btn_mode) == 1 and GPIO.input(btn_rec) == 1: #Check that position switch is in position 3
        print("switch pos1: " + str(GPIO.input(swch_pos1)))
        print("switch pos3: " + str(GPIO.input(swch_pos3)))
        time.sleep(0.15)
        btn_C.when_pressed = C5.play
        btn_Db.when_pressed = Db5.play
        btn_D.when_pressed = D5.play
        btn_Eb.when_pressed = Eb5.play
        btn_E.when_pressed = E5.play
        btn_F.when_pressed = F5.play #Play 5th octave notes
        btn_Gb.when_pressed = Gb5.play
        btn_G.when_pressed = G5.play
        btn_Ab.when_pressed = Ab5.play
        btn_A.when_pressed = A5.play
        btn_Bb.when_pressed = Bb5.play
        btn_B.when_pressed = B5.play
        
    if GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 0:
        print("Mode Btn: " + str(GPIO.input(btn_mode)))
        print("Record Btn: " + str(GPIO.input(btn_rec)))
        time.sleep(0.15)
        btn_C.when_pressed = custom1.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom1.wav')
        btn_Db.when_pressed = custom2.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom2.wav')
        btn_D.when_pressed = custom3.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom3.wav')
        btn_Eb.when_pressed = custom4.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom4.wav')
        btn_E.when_pressed = custom5.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom5.wav')
        btn_F.when_pressed = custom6.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom6.wav')
        btn_Gb.when_pressed = custom7.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom7.wav')
        btn_G.when_pressed = custom8.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom8.wav')
        btn_Ab.when_pressed = custom9.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom9.wav')
        btn_A.when_pressed = custom10.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom10.wav')
        btn_Bb.when_pressed = custom11.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom11.wav')
        btn_B.when_pressed = custom12.record(5, output='/home/pi/gpio-music-box/CustomSounds/custom12.wav')
    elif GPIO.input(btn_mode) == 0 and GPIO.input(btn_rec) == 1:
        print("Mode Btn: " + str(GPIO.input(btn_mode)))
        print("Record Btn: " + str(GPIO.input(btn_rec)))
        time.sleep(0.15)
        btn_C.when_pressed = custom1.play
        btn_Db.when_pressed = custom2.play
        btn_D.when_pressed = custom3.play
        btn_Eb.when_pressed = custom4.play
        btn_E.when_pressed = custom5.play
        btn_F.when_pressed = custom6.play
        btn_Gb.when_pressed = custom7.play
        btn_G.when_pressed = custom8.play
        btn_Ab.when_pressed = custom9.play
        btn_A.when_pressed = custom10.play
        btn_Bb.when_pressed = custom11.play
        btn_B.when_pressed = custom12.play