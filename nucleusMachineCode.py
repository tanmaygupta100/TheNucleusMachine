#Name: Tanmay Gupta
#Project: The Nucleus Machine
#Description:
    # The ultimate study tool in one machine,
    # providing the following features:
        # Ambient Sound Player
        # RGB Light Mode
        # Rotating Segment Timer


import pygame #not yet installed, for headphone jack
from gpiozero import Button, LED, Buzzer
from time import sleep


# Define GPIO pins for buttons and LED:
timerButton = Button(17, bounce_time=0.5)
timer_segments = [LED(22), LED(23), LED(24), LED(25), LED(8), LED(7), LED(12)] # F, A, B, C, D, E, G
lightButton = Button(18, bounce_time=0.5)
rgbLED = LED(21)
musicButton = Button(27, bounce_time=0.5)

# Timer variables
current_segment = 0
timer_running = False

# LED light variables
light_on = False
light_modes = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # Red, Green, Blue
light_mode_index = 0

# Ambient sound variables
sounds = ["birdswind.mp3", "whalesocean.mp3", "airplane.mp3", "coffeeshop.mp3"]
current_sound = 0
sound_playing = False

# Function to play the current sound
def play_sound():
    global sound_playing
    if not sound_playing:
        sound_playing = True
        # Add code to play the current sound file
        print(f"Playing: {sounds[current_sound]}")

# Function to stop the current sound
def stop_sound():
    global sound_playing
    sound_playing = False
    # Add code to stop the current sound
    print("Stopping current sound")

# Function to start the timer
def start_timer():
    global timer_running, current_segment
    timer_running = True
    while timer_running and current_segment < 7:
        timer_segments[current_segment].on()
        sleep(1)  # Flashing interval
        timer_segments[current_segment].off()
        sleep(1)
        current_segment += 1
    if current_segment == 7:
        # Timer completed
        current_segment = 0
        timer_running = False

# Function to reset the timer
def reset_timer():
    global current_segment, timer_running
    for segment in timer_segments:
        segment.off()
    current_segment = 0
    timer_running = False

# Function to toggle the LED light
def toggle_light():
    global light_on
    light_on = not light_on
    if light_on:
        led.color = light_modes[light_mode_index]
    else:
        led.off()

# Function to change the LED light mode
def change_light_mode():
    global light_mode_index
    light_mode_index = (light_mode_index + 1) % len(light_modes)
    if light_on:
        led.color = light_modes[light_mode_index]

# Assign functions to button events
timer_button.when_pressed = start_timer
timer_button.when_released = reset_timer
led_button.when_pressed = toggle_light
led_button.when_held = change_light_mode
music_button.when_pressed = play_sound
music_button.when_held = stop_sound

try:
    while True:
        sleep(0.1)  # Keep the program running

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Cleanup GPIO on program exit
    for segment in timer_segments:
        segment.off()
    led.off()
    # Add code to stop any playing sound
    print("Cleanup complete.")
