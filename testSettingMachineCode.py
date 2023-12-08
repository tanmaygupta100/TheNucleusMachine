from time import sleep

# Timer variables
current_segment = 0
timer_running = False

# LED light variables
light_on = False
light_modes = ["Red", "Green", "Blue"]
light_mode_index = 0

# Ambient sound variables
sounds = ["birdswind.mp3", "whalesocean.mp3", "airplane.mp3", "coffeeshop.mp3"]
current_sound = 0
sound_playing = False

# Function to play the current sound or stop the player
def toggle_sound():
    global sound_playing, current_sound
    if sound_playing:
        sound_playing = False
        print("Stopping current sound")
    else:
        sound_playing = True
        # Add code to print the current sound file
        print(f"Playing: {sounds[current_sound]}")

# Function to skip to the next audio and start playing it
def skip_and_play_sound():
    global current_sound
    toggle_sound()  # Toggle the sound player off
    current_sound = (current_sound + 1) % len(sounds)
    toggle_sound()  # Toggle the sound player on and start playing the next sound


# Function to start the timer
def start_timer():
    global timer_running, current_segment
    timer_running = True
    while timer_running and current_segment < 7:
        print(f"Segment: {chr(ord('A') + current_segment)}")
        sleep(1)  # Flashing interval
        current_segment += 1
    if current_segment == 7:
        # Timer completed
        current_segment = 0
        timer_running = False

# Function to reset the timer
def reset_timer():
    global current_segment, timer_running
    current_segment = 0
    timer_running = False

# Function to toggle the LED light
def toggle_light():
    global light_on
    light_on = not light_on
    if light_on:
        print(f"RGB Light Mode: {light_modes[light_mode_index]}")
    else:
        print("RGB Light Mode: Off")

# Function to change the LED light mode
def change_light_mode():
    global light_mode_index
    light_mode_index = (light_mode_index + 1) % len(light_modes)
    if light_on:
        print(f"RGB Light Mode: {light_modes[light_mode_index]}")

try:
    while True:
        command = input("Enter command (t, t+t, l, l+l, m, m+m): ")

        if command == "t":
            start_timer()
        elif command == "t+t":
            reset_timer()
        elif command == "l":
            toggle_light()
        elif command == "l+l":
            change_light_mode()
        elif command == "m":
            toggle_sound()
        elif command == "m+m":
            skip_and_play_sound()
        else:
            print("Invalid command. Please enter a valid command.")

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    print("Cleanup complete.")


'''
SAMPLE OUTPUTS:
_____________________________________________
Enter command (t, t+t, l, l+l, m, m+m): m
Playing: birdswind.mp3
Enter command (t, t+t, l, l+l, m, m+m): m
Stopping current sound
Enter command (t, t+t, l, l+l, m, m+m): m
Playing: birdswind.mp3
Enter command (t, t+t, l, l+l, m, m+m): m+m
Stopping current sound
Playing: whalesocean.mp3
Enter command (t, t+t, l, l+l, m, m+m): m+m
Stopping current sound
Playing: airplane.mp3
Enter command (t, t+t, l, l+l, m, m+m): m
Stopping current sound
Enter command (t, t+t, l, l+l, m, m+m): t
Segment: A
Segment: B
Segment: C
Segment: D
Segment: E
Segment: F
Segment: G
Enter command (t, t+t, l, l+l, m, m+m): l
RGB Light Mode: Red
Enter command (t, t+t, l, l+l, m, m+m): l+l
RGB Light Mode: Green
Enter command (t, t+t, l, l+l, m, m+m): l
RGB Light Mode: Off
_____________________________________________
'''
