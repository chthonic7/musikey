# musikey
A python script for musical typing

## Overview

This is a simple script, inspired by pydub, that reads your keystrokes and produces notes according to which key is pressed. Special keys such as "shift" or "ctrl" modify the notes produced by going up and down an octave. To stop the script, press the '0'(zero) key.

As the project stands, the script is restricted to linux systems that use the X Window manager. This is because it leverages the xinput utility to read keystrokes.

For best results, one should disable key repeats on holding down a key and also run the script as a background process. My favorite way of doing this is by starting the script in a tmux session and then detaching it.

## Installation

This project requires Python 3 as well as the installation of pyaudio, which readily available through pip. You will also need to have xinput installed, which should be available through most package managers.

## To-Do
1. Extend key-note mappings to whole keyboard
2. Let the script automagically run in the background.
3. Port to other systems, such as Windows.
