# audio-synthesis-in-python
audioSynth.py is a module that alows the user to produce numpy arrays that
can be set to the speakers as sound by modules like "simpleaudio" or
"sounddevices". run "python3 synth_base.py" in your terminal or cmd promt
after installing the modules in the requirments section below. then wait for
program to tell you that it loaded in X seconds, and you're ready to play!


### Requirments:

python3 (3.6 or higher)
numpy
scipy
simpleaudio
pygame


### Mapping:
~~~
 w e   t y u   o p 
a s d f g h j k l ;
~~~
its just like a piano with the note "C" being mapped to the keyboard key "a".
if you hold down the shift key (or use the caps lock key) you can get notes
that are an octave lower.