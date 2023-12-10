# TheNucleusMachine
The Nucleus Machine is a simplistic study tool built with Python and Raspberry Pi, using Linux and wired hardware.

Features:
* Ambient Sounds Player
  * Plays different ambient sounds, or white noises.
  * Helps reduce auditory distractions and increase focus during work.
* Rotating Segment Timer
  * A 7-segment display displays a rotating animation.
  * The timer can be set for 5 minutes and can be interrupted or reset at any moment in time.
* LED Light Modes
  * Different light modes to indicate study/break periods.
  * Focus mode uses cool lighting for more intense studying that requires deeper focus.
  * Reading/relaxing mode uses warm lighting for allowing eyes to adjust and relax.


How it works:
* Audio button:
 * Turns on the Ambient Sounds Player, playing the first audio in the queue.
 * Can skip through other audios, or go back to the initial state.
 * Components: Single button, speaker.
* Timer button:
 * Turns on the Rotating Segment Timer, in which it repeats a spirling animation of segments F, A, B, C, D, E, G, DP.
 * The segments may be reset as desired using an additional button press at any point.
 * The animation repeats until 5 minutes is reached, at which point the DP segment will indicate that the time is over.
* LED button:
 * Turns on the LED Lights, turning on the focus mode first.
 * Another button press switches to the relax mode.
 * A 3rd click turns off the feature


Files:
* nucleusMachine.py
  * Code runs on the Raspberry Pi.
  * Uses Pi button inputs and hardware outputs.
* testSettingMachineCode.py
  * Similar code for testing through keyboard inputs and terminal outputs.
  * Meant to test the code while ensuring the hardware components aren't shortcircuited due to faulty code.
