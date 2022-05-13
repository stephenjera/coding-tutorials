"""
This code uses a Matlab file to create simulated audio data for musical notes

Every note will have: pluck position
"""

# TODO modify create wav to include time shifting

import matlab.engine
import os
from Notes_to_Frequency import notes_to_frequency

directory = "Simulated_Dataset_Matlab_12frets"  # name of directory to create
# Pluck position is audable symtric from 0.5, e.g 0.7 = 0.3 (kind of)
PLUCK_POSITIONS = [0, 0.5, 0.7, 0.9]  # listening to the notes these showed noticeble diferences
DETUNE_FREQUENCIES = [-2, -1, 0, 1, 2]


def create_wav(filename, freq, pluck_position=0.9, excitation_signal='excite-picked-nodamp.wav'):
    """
    Creates a wav file for the specified frequency
            :param filename: name of note
            :param freq: note frequency
            :param pluck_position: simulate pluck position on guitar
            :param excitation_signal: signal used to create notes
    """
    eng = matlab.engine.start_matlab()  # start matlab engine
    e = eng.audioread(excitation_signal)
    e = eng.transpose(e)

    fs = eng.double(44100)  # sample rate

    # loop filter:
    B = eng.cell2mat(eng.cell([eng.double(0.8995), eng.double(0.1087)]))
    A = eng.cell2mat(eng.cell([eng.double(1), eng.double(0.0136)]))

    # o = eng.double(3)   # octave
    nd = eng.double(4)  # note duration
    p = eng.double(pluck_position)  # pluck position
    l = eng.kspluck(eng.double(freq), nd, fs, e, B, A, p)

    # Bits per sample > 16 to prevent clipping
    eng.audiowrite(filename, l, fs, 'BitsPerSample', 32, nargout=0)


def play_style(path, note_name, excitation, pluck_pos):
    """
    create notes with different play styles
    :param path: place to create file
    :param note_name: name of the note to create
    :param excitation: picked or plucked excitation signal
    :param pluck_pos: position to pluck
    """
    pluck_pos = float(pluck_pos)  # convert from numpy float
    pluck_int = int(pluck_pos*10)  # remove decimal from pluck position
    pluck_str = str(pluck_int)
    if excitation == "excite-picked-nodamp.wav":
        style = "Picked"
    else:
        style = "Plucked"
    for freq_shift in DETUNE_FREQUENCIES:
        #freq_shift = i - (notes_num / 2)  #TODO change so scaling is better
        new_freq = value + freq_shift
        print("New frequency: ", new_freq)
        created_path = path + "\\" + note_name + "_" + str(freq_shift) + "_" + style + "_" + pluck_str + ".wav"
        create_wav(filename=created_path, freq=new_freq, excitation_signal=excitation, pluck_position=pluck_pos)
        print("Created: ", created_path)


if __name__ == "__main__":
    # create the directory
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory '% s' created" % directory)
    else:
        print("Already a directory")

    for key, value in notes_to_frequency.items():
        # create notes directory
        note_path = os.path.join(directory, key)
        # if path does not exist create it
        if not os.path.exists(note_path):
            os.mkdir(note_path)
            # Loop through for all pluck positions from 0.1 to 1 in steps of 0.3
            for pluck in PLUCK_POSITIONS:
                # create frequency shifted notes for picked
                play_style(path=note_path, note_name=key, excitation="excite-picked-nodamp.wav", pluck_pos=pluck)
                # create frequency shifted notes for plucked
                play_style(path=note_path, note_name=key, excitation="excite-plucked-nodamp.wav", pluck_pos=pluck)

            """
            for j in range(notes_num):
                freq_shift = j - (notes_num/2)
                new_freq = value + freq_shift
                print("New frequency: ", new_freq)
                # unmodified note will be j == notes_num/2
                create_wav(filename=note_path + "\\" + key + "_" + str(j) + "_Picked" + ".wav", freq=new_freq)
                print("Created: " + note_path + "\\" + key + "_" + str(j) + "_Picked" + ".wav")

            # frequency shift loop for excite-plucked-nodamp.wav
            for k in range(notes_num):
                freq_shift = k - (notes_num/2)
                new_freq = value + freq_shift
                print("New frequency: ", new_freq)
                # unmodified note will be j == notes_num/2
                create_wav(filename=note_path + "\\" + key + "_" + str(k) + "Plucked" + ".wav", freq=new_freq)
                print("Created: " + note_path + "\\" + key + "_" + str(k) + "Plucked" + ".wav")
"""
            print("Directory '% s' created" % key)

        else:
            print("Already a directory")
