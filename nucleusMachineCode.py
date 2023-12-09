#Name: Tanmay Gupta
#Project: The Nucleus Machine
#Description:
    # The ultimate study tool in one machine,
    # providing the following features:
        # Ambient Sound Player
        # RGB Light Mode
        # Rotating Segment Timer


import pygame
from gpiozero import Button, LED
from time import sleep

# Initialize pygame mixer
pygame.mixer.init()

# Define GPIO pins for buttons and LED:
timer_button = Button(5, bounce_time=0.5)
timer_segments = [LED(12), LED(10), LED(22), LED(21), LED(23), LED(27), LED(16)]  # F, A, B, C, D, E, G
dp_segment = LED(19)  # Decimal point segment
light_button = Button(38, bounce_time=0.5)
rgb_led = LED(40)
music_button = Button(3, bounce_time=0.5)

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
        pygame.mixer.music.load(sounds[current_sound])
        pygame.mixer.music.play()

# Function to stop the current sound
def stop_sound():
    global sound_playing
    if sound_playing:
        pygame.mixer.music.stop()
        sound_playing = False
        print("Stopping current sound")

# Function to start the timer
def start_timer():
    global timer_running, current_segment
    timer_running = True
    while timer_running and current_segment < 7:
        timer_segments[current_segment].on()
        dp_segment.toggle()  # Toggle decimal point segment
        sleep(1)  # Flashing interval
        timer_segments[current_segment].off()
        dp_segment.toggle()  # Toggle decimal point segment
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
    dp_segment.off()  # Turn off decimal point segment
    current_segment = 0
    timer_running = False

# Function to toggle the LED light
def toggle_light():
    global light_on
    light_on = not light_on
    if light_on:
        rgb_led.color = light_modes[light_mode_index]
    else:
        rgb_led.off()

# Function to change the LED light mode
def change_light_mode():
    global light_mode_index
    light_mode_index = (light_mode_index + 1) % len(light_modes)
    if light_on:
        rgb_led.color = light_modes[light_mode_index]

# Assign functions to button events
timer_button.when_pressed = start_timer
timer_button.when_released = reset_timer
light_button.when_pressed = toggle_light
light_button.when_held = change_light_mode
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
    dp_segment.off()
    rgb_led.off()
    # Add code to stop any playing sound
    print("Cleanup complete.")
