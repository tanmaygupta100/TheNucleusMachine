# TheNucleusMachine
The Nucleus Machine is a simplistic study tool built with Python and Raspberry Pi, using Linux and wired hardware.

Features:
* Ambient Sounds Player
  * Plays different ambient sounds, or white noises.
  * Helps reduce auditory distractions and increase focus during work.
  * Single-click:
    * Starts playing the audio. Stops the audio and resets the queue.
  * Double-click:
    * Skips to the next audio, cycling through the audios.
* Rotating Segment Timer
  * A 7-segment display flashes every other second.
  * After 5 minutes, the current segment lights fully, and moves onto the next segment, in a spiral pattern.
  * Single-click:
    * Starts or stops and resets the timer and segment lights.
  * Double-click:
    * Plays or pauses the timer and lights.
* RGB LED Modes
  * Different light modes to indicate study/break periods.
  * Single-click:
    * Turns on/off the RGB LED.
  * Double-click:
    * Cycles between different RGB settings.


Files:
* nucleusMachineCode.py
  * Code meant to run on the Raspberry Pi.
  * Uses Pi inputs and hardware outputs.
* testSettingMachineCode.py
  * Similar code for testing through keyboard inputs and terminal outputs.
  * Meant to test the code while ensuring the hardware components aren't shortcircuited due to faulty code.
