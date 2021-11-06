import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

# y = A*sin(w*t + phase) = A*sin(2*pi*f*t + phase)

sr = 44100.0  # sample rate (hertz)
T = 1/sr  # period for 1 sample
t = 10  # how log to generate signal (seconds)
N = sr * t  # number of data points (time)
f = 73.42  # frequency
omega = 2*np.pi*f  # angular frequency
t_seq = np.arange(N)*T
A = 10  # amplitude

y = A*np.sin(omega*t_seq)
plt.plot(t_seq, y)
#plt.show()

obj = wave.open("sound.wav", "w")
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(sr)

for i in y:
    print(i)
    data = struct.pack("b", int(i))
    obj.writeframesraw(data)
obj.close()

