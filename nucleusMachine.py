#Name: Tanmay Gupta
#Project: The Nucleus Machine
#Description:
    # The ultimate study tool in one machine,
    # providing the following features:
        # Ambient Sound Player
        # LED Light Mode
        # Rotating Segment Timer

import pygame # library for playing audio out of the speakers
import os # library used to access files for playing audio
from gpiozero import Button, LED # library to use the buttons and LEDs
from time import sleep # library for timer related actions


# Defining GPIO pins for buttons, LEDs, and segments:
# Rotating Timer pins:
timerButton = Button(3) #pin 5
segmentF = LED(18) # pin 12
segmentA = LED(15) # pin 10
segmentB = LED(14) # pin 22
segmentC = LED(9) # pin 21
segmentD = LED(11) # pin 23
segmentE = LED(0) # pin 27
segmentG = LED(23) # pin 16
segmentDP = LED(10)  # Decimal point segment, pin 19
# LED Light Mode pins:
ledButton = Button(20) #pin 38
whiteLed = LED(21) #pin 40
yellowLed = LED(26) #pin 37
# Ambient Sound Player pins:
audioButton = Button(2) #pin 3


# Initializing global state variable:
state = 0
# Placing the segments into an array for a sequential call:
sequence = [segmentF, segmentA, segmentB, segmentC, segmentD, segmentE, segmentF, segmentG, segmentDP]

# Accessing the files from the Raspberry Pi's Linux-based desktop:
folder_path = os.path.expanduser("~/Desktop/Nucleus")
audio_files = ["rainthunder.mp3", "rainthunder.mp3", "naturesounds.mp3", "whitenoise.mp3"]
pygame.mixer.init() # Initializing the pygame mixer
current_audio_index = 0


# LED FUNCTION:
    # ledFunction - Controls the states of the LEDs, incrementally adjusting with each 
def ledFunction(): # This function controls 
    global state
    state += 1 # The state changes incrementally with each call of the ledFunction.
    if state == 1: # Button was pressed once to turn on the white LED.
        whiteLed.on()
    elif state == 2: # BUtton was pressed a 2nd time to switch to the yellow LED.
        whiteLed.off()
        yellowLed.on()
    elif state == 3: # Button was pressed a 3rd time to turn off all lights.
        whiteLed.off()
        yellowLed.off()
        state = 0 # Resetting the state in the 3rd click state


# TIMER FUNCTIONS:
    # playTimer - Starts the timer or stops it based on button inputs.
    # timerFunction - Automated segment light sequence repeats until interrupted by a button input.
def playTimer():
    global state
    state += 1
    if state == 1:
        timerFunction()
    elif state == 2:
        for segment in sequence:
            segment.off()
        segmentDP.off()
        state = 0
def timerFunction():
    global state
    for _ in range(300): #runs for 5 minutes
        for segment in sequence:
            segment.on()
            sleep(0.125)
            if timerButton.is_pressed:
                for segment in sequence:
                    segment.off()
                segmentDP.off()
                state = 0
                sleep(0.125)
                return
        for segment in sequence:
            segment.off()
    segmentDP.on() # DP stays on at the end to let you know the timer is over
    state = 2
        

# AUDIO FUNCTIONS:
    # playAudio - Loads and plays the specific audio files.
    # audioFunction - Stops current audio and incrementally moves up to the next song.
def playAudio(file_name):
    file_path = os.path.join(folder_path, file_name)
    print("Playing: ", repr(file_path)) # Line for debugging
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def audioFunction():
    global current_audio_index
    pygame.mixer.music.stop() # stop currently playing audio
    current_audio_index += 1 # incrementing the audio index
    # checking if reached the end of the playlist:
    if 0 <= current_audio_index < len(audio_files):
        playAudio(audio_files[current_audio_index])
    else:
        current_audio_index = 0 # if reached the end of the playlist, it goes to the first index, playing nothing.
        

# Button-input commands for the 3 features:
ledButton.when_pressed = ledFunction # LED
timerButton.when_pressed = playTimer # Timer
audioButton.when_pressed = audioFunction # Audio


# Code to keep the program running or provide termination fallback/cleanup:
try:
    while True:
        sleep(0.1)  # Keep the program running

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Cleanup GPIO on program exit
    for segment in sequence:
        segment.off()
    segmentDP.off()
    whiteLed.off()
    yellowLed.off()
    pygame.mixer.quit()
    print("Cleanup complete.")
