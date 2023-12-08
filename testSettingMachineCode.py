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

# Function to play the current sound
def play_sound():
    global sound_playing
    if not sound_playing:
        sound_playing = True
        # Add code to print the current sound file
        print(f"Playing: {sounds[current_sound]}")

# Function to stop the current sound
def stop_sound():
    global sound_playing
    sound_playing = False
    # Add code to print the stopping message
    print("Stopping current sound")

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
            play_sound()
        elif command == "m+m":
            stop_sound()
        else:
            print("Invalid command. Please enter a valid command.")

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    print("Cleanup complete.")
