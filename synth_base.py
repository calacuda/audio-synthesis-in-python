"""
==============================================================================
******************************************************************************
********************+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+**********************
************************|                          |**************************
************************| - synth_with_numpy8.py - |**************************
************************|                          |**************************
********************+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+**********************
******************************************************************************
==============================================================================

synth_with_numpy8.0.py
A part of the interactive_synth.py project
python version :  3.6.8


project notes:
this program will hopefully be a synthesiser that the user can interact with
via the key board or a MIDI controller. It uses, the vanilla time module from
python along with the modules, numpy, scipy, pygame, and simpleaudio.

version notes:
This make "normal" note just the single  waveform that is an amalgam a number
of overtones equivalent to of how ever many oscillators you have engaged.

By: Eoghan West | licences: anti-licence |version: 1.0 |
development start: 2-4-19 | current development: 5-10-19 |
development end: ?
"""


import pygame
import simpleaudio as sa
import time
from audioSynth import Synthosizar

program_init_time = time.time()
pygame.init()

win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("--v8.0--")


synth_wavetype = 'sin'

synth = Synthosizar(wave_type=synth_wavetype, use_osc2=True, use_osc3=True,
                    # use_osc4=True, use_osc5=True, use_osc6=True,
                    # use_osc7=True, use_osc8=True, use_osc9=True,
                    volume=0.1)

print("making note, doing math")
###################################
C2 = 65
Note_C2 = synth.make_note(C2)
print("Note_C2 assigned")
CS2 = 69
Note_CS2 = synth.make_note(CS2)
print("Note_CS2 assigned")
D2 = 73
Note_D2 = synth.make_note(D2)
print("Note_D2 assigned")
DS2 = 78
Note_DS2 = synth.make_note(DS2)
print("Note_DS2 assigned")
E2 = 82.4
Note_E2 = synth.make_note(E2)
print("Note_E2 assigned")
F2 = 87.3
Note_F2 = synth.make_note(F2)
print("Note_F2 assigned")
FS2 = 92.5
Note_FS2 = synth.make_note(FS2)
print("Note_FS2 assigned")
G2 = 98.0
Note_G2 = synth.make_note(G2)
print("Note_G2 assigned")
GS2 = 103.8
Note_GS2 = synth.make_note(GS2)
print("Note_GS2 assigned")
A2 = 110.0
Note_A2 = synth.make_note(A2)
print("Note_A2 assigned")
AS2 = 116.5
Note_AS2 = synth.make_note(AS2)
print("Note_AS2 assigned")
B2 = 123.5
Note_B2 = synth.make_note(B2)
print("Note_B2 assigned")
###################################
C3 = 130.8
Note_C3 = synth.make_note(C3)
print("Note_C3 assigned")
CS3 = 138.6
Note_CS3 = synth.make_note(CS3)
print("Note_CS3 assigned")
D3 = 146.8
Note_D3 = synth.make_note(D3)
print("Note_D3 assigned")
DS3 = 155.6
Note_DS3 = synth.make_note(DS3)
print("Note_DS3 assigned")
E3 = 164.8
Note_E3 = synth.make_note(E3)
print("Note_E3 assigned")
F3 = 174.6
Note_F3 = synth.make_note(F3)
print("Note_F3 assigned")
FS3 = 185.0
Note_FS3 = synth.make_note(FS3)
print("Note_FS3 assigned")
G3 = 196.0
Note_G3 = synth.make_note(G3)
print("Note_G3 assigned")
GS3 = 207.7
Note_GS3 = synth.make_note(GS3)
print("Note_GS3 assigned")
A3 = 220.0
Note_A3 = synth.make_note(A3)
print("Note_A3 assigned")
AS3 = 233.1
Note_AS3 = synth.make_note(AS3)
print("Note_AS3 assigned")
B3 = 246.9
Note_B3 = synth.make_note(B3)
print("Note_B3 assigned")
###################################
C4 = 261.6
Note_C4 = synth.make_note(C4)
print("Note_C4 assigned")
CS4 = 277.2
Note_CS4 = synth.make_note(CS4)
print("Note_CS4 assigned")
D4 = 293.7
Note_D4 = synth.make_note(D4)
print("Note_D4 assigned")
DS4 = 311.1
Note_DS4 = synth.make_note(DS4)
print("Note_DS4 assigned")
E4 = 329.6
Note_E4 = synth.make_note(E4)
print("Note_E4 assigned")


key_lookup = {
              'a': Note_C3, 'w': Note_CS3, 's': Note_D3, 'e': Note_DS3,
              'd': Note_E3, 'f': Note_F3, 't': Note_FS3, 'g': Note_G3,
              'y': Note_GS3, 'h': Note_A3, 'u': Note_AS3, 'j': Note_B3,
              'k': Note_C4, 'o': Note_CS4, 'l': Note_D4, 'p': Note_DS4,
              ';': Note_E4,
              'A': Note_C2, 'W': Note_CS2, 'S': Note_D2, 'E': Note_DS2,
              'D': Note_E2, 'F': Note_F2, 'T': Note_FS2, 'G': Note_G2,
              'Y': Note_GS2, 'H': Note_A2, 'U': Note_AS2, 'J': Note_B2,
              'K': Note_C3, 'O': Note_CS3, 'L': Note_D3, 'P': Note_DS3,
              ':': Note_E3,
              }

print("program loaded in, {}, second(s).".format(time.time() -
                                                 program_init_time))


def main():
    """
    main body, responsible for running the show.
    :return:
    """
    start_chime = sa.play_buffer(Note_B3, 1, 2, 44100)
    time.sleep(.2)
    start_chime.stop()
    pygame.key.set_repeat()
    playing = {}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                current_key = event.unicode
                if current_key == '':
                    break

                try:
                    note = key_lookup.get(current_key)
                    print(current_key)
                    note = sa.play_buffer(note, 1, 2, 44100)
                    playing[event.key] = note
                except TypeError:
                    break
            elif event.type == pygame.KEYUP:
                while event.key in playing:
                    playing.get(event.key).stop()
                    del playing[event.key]
            else:
                break


main()
