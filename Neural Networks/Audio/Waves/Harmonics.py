import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import os
import random

directory = "Harmonics_Test"
# Parent Directory path
parent_dir = ""
# Path
# path = os.path.join(parent_dir, directory)
path = directory
sr = 44100.0  # sample rate (hertz)


def create_wav(filename, freq, sample_rate=44100.0,  amplitude=20, num_harmonics=1):
    # y = A*sin(2*pi*nf_1*t + phase)
    period = 1/sample_rate  # period for 1 sample
    print("Period: {}".format(period))
    t = 10  # how log to generate signal (seconds)
    n = sr * t  # number of data points (no unit)
    print("Number of data points: {}".format(n))
    omega = 2*np.pi*freq  # angular frequency
    print("omega: {}".format(omega))
    t_seq = np.arange(n)*period
    print("tseq: {}".format(t_seq))

    y_final = []
    y = []
    for i in range(1, num_harmonics+1):
        print("num_harmonics: {}".format(num_harmonics))
        print(("i: {}".format(i)))
        y_temp = y  # y_temp need to save the last value of y
        y = amplitude*np.sin(i*omega*t_seq)
        amplitude = amplitude/2
        if i > 1:
            y_final = [sum(x) for x in zip(y, y_temp)]
        else:
            print("skipped")
    """
    plt.subplot(211)
    plt.ylabel("Amplitude")
    plt.xlabel("time")
    plt.plot(t_seq, y_final)

    plt.subplot(212)
    plt.plot(t_seq, y)
    plt.ylabel("Amplitude")
    plt.xlabel("time")
    plt.show()
    """
    obj = wave.open(filename+".wav", "w")
    obj.setnchannels(1)  # mono
    obj.setsampwidth(2)
    obj.setframerate(sr)

    for i in y_final:
        print(i)
        data = struct.pack("b", int(i))
        obj.writeframesraw(data)
    obj.close()


if __name__ == "__main__":
    create_wav(filename=directory, sample_rate=sr, freq=440, amplitude=60, num_harmonics=5)
