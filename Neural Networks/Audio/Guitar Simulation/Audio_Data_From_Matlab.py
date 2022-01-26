"""
This code uses a Matlab file to create simulated audio data for musical notes
"""

import matlab.engine
import os
import random
from Notes_to_Frequency import notes_to_frequency

directory = "Simulated_Dataset_Matlab"

random.seed(20)


def create_wav(filename, freq, pluck_position=0.9):
    eng = matlab.engine.start_matlab()
    e = eng.audioread('excite-picked-nodamp.wav')
    e = eng.transpose(e)

    fs = eng.double(44100)  # sample rate

    # loop filter:
    B = eng.cell2mat(eng.cell([eng.double(0.8995), eng.double(0.1087)]))
    A = eng.cell2mat(eng.cell([eng.double(1), eng.double(0.0136)]))

    # o = eng.double(3)   # octave
    nd = eng.double(4)  # note duration
    p = eng.double(pluck_position)  # pluck position
    l = eng.kspluck(eng.double(freq), nd, fs, e, B, A, p)

    eng.audiowrite(filename, l, fs, nargout=0)


if __name__ == "__main__":
    # Create the directory
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory '% s' created" % directory)
    else:
        print("Already a directory")

    for key, value in notes_to_frequency.items():
        # create notes directory
        note_path = os.path.join(directory, key)
        if not os.path.exists(note_path):
            os.mkdir(note_path)
            # generate correct pitch signal
            create_wav(filename=note_path + "\\" + key + ".wav", freq=value)  # ".wav" required for audiowrite
            print("Created: " + note_path + "\\" + key + ".wav")
            for j in range(10):
                # amplitude_random = random.randint(5, 20)
                freq_shift = random.uniform(-10, 10)  # random float to change frequency
                new_freq = value + freq_shift
                # append a number up to 10 to identify modified data
                create_wav(filename=note_path + "\\" + key + str(j) + ".wav", freq=new_freq)
                print("Created: " + note_path + "\\" + key + str(j) + ".wav")
            print("Directory '% s' created" % key)
        else:
            print("Already a directory")
