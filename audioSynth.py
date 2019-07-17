"""
audioSynth.py

a module disined to create numpy arrays that are representative of digital sine 
waves. they can therefor be sent to a module like "simpleaudio" to be played
through the systems speakers.

By: Calacuda  |  MIT licence  |  initial release  : July, 2019  |
"""

import numpy as np
import scipy.signal


class Oscillator:
    def __init__(self, attenuation=0.3, transposition=1, wave_type='sin',
                 sample_rate=44100):
        self.atten = attenuation
        self.transposition = transposition
        self.samp_rate = sample_rate
        self.each_sample_number = np.arange(60 * self.samp_rate)
        self.wave_type = wave_type

    def make_wave(self, frequency):
        frequency *= self.transposition
        t = np.linspace(0, 60, 60 * self.samp_rate, False)
        if self.wave_type == 'sin':
            waveform = np.sin(frequency * t * 2 * np.pi)
        elif self.wave_type == 'squ':
            waveform = (scipy.signal.square(
                        frequency * t * 2 * np.pi)) * (self.atten * 0.1)
        elif self.wave_type == 'saw':
            waveform = (scipy.signal.sawtooth(
                        frequency * t * 2 * np.pi)) * (self.atten * 0.1)
        elif self.wave_type == 'tri':
            waveform = (scipy.signal.sawtooth(
                        frequency * t * 2 * np.pi)) * self.atten
        else:
            raise ValueError("wave_type must be one of the following, 'sin'," 
                             "'squ', 'saw', or 'tri'")
        waveform += waveform
        waveform += waveform + waveform
        waveform += waveform

        return waveform

    def get_atten(self):
        return self.atten


class Synthosizar:
    def __init__(self, osc1_attenuation=0.3, wave_type='sin', use_osc2=False,
                 osc2_attenuation=0.25, osc2_octave=2, use_osc3=False,
                 osc3_attenuation=0.19, osc3_octave=3, use_osc4=False,
                 osc4_attenuation=0.16, osc4_octave=4, use_osc5=False,
                 osc5_attenuation=0.10, osc5_octave=5, use_osc6=False,
                 osc6_attenuation=0.07, osc6_octave=6, use_osc7=False,
                 osc7_attenuation=0.05, osc7_octave=7, use_osc8=False,
                 osc8_attenuation=0.02, osc8_octave=8, use_osc9=False,
                 osc9_attenuation=0.02, osc9_octave=9, volume=1.0):
        self.osc1 = Oscillator(attenuation=osc1_attenuation,
                               wave_type=wave_type)
        self.wave_type = wave_type
        self.volume = volume
        self.osc_atten = [osc1_attenuation]
        self.osc_s = []
        osc_settings = [(use_osc2, osc2_attenuation, osc2_octave),
                        (use_osc3, osc3_attenuation, osc3_octave),
                        (use_osc4, osc4_attenuation, osc4_octave),
                        (use_osc5, osc5_attenuation, osc5_octave),
                        (use_osc6, osc6_attenuation, osc6_octave),
                        (use_osc7, osc7_attenuation, osc7_octave),
                        (use_osc8, osc8_attenuation, osc8_octave),
                        (use_osc9, osc9_attenuation, osc9_octave)]
        for use, atten, octave in osc_settings:
            if use:
                new_osc = Oscillator(atten, octave, wave_type)
                self.osc_s.append(new_osc)
                self.osc_atten.append(atten)
        self.osc_atten = sum(self.osc_atten)

    def make_note(self, frequency):
        note = self.osc1.make_wave(frequency)
        for osc in self.osc_s:
            note += osc.make_wave(frequency)
        note *= (1.0 / self.osc_atten / 2)
        note *= self.volume
        note *= 32767 / max(abs(note))
        note = note.astype(np.int16)
        return note

    def manual_note(self, frequency):
        note = self.osc1.make_wave(frequency)
        for osc in self.osc_s:
            note += osc.make_wave(frequency)
        note *= (1.0 / self.osc_atten / 2)
        note *= self.volume
        return note

    def make_chord(self, freq_hz_lst):
        chordal_wave = self.make_note(freq_hz_lst[0])
        for freq_Hz in freq_hz_lst[1:]:
            chordal_wave += self.make_note(freq_Hz)
        else:
            pass
        chordal_wave /= float(len(freq_hz_lst))
        return chordal_wave

