import matlab.engine
import numpy as np
eng = matlab.engine.start_matlab()

e = eng.audioread('excite-picked-nodamp.wav')
e = eng.transpose(e)

fs = eng.double(44100)

# loop filter:
B = eng.cell2mat(eng.cell([eng.double(0.8995), eng.double(0.1087)]))
A = eng.cell2mat(eng.cell([eng.double(1), eng.double(0.0136)]))
# B = eng.double([0.8995, 0.1087])
# A = eng.double([1, 0.0136])

o = eng.double(3)   # octave
nd = eng.double(2.0)  # note duration
p = eng.double(.9)  # pluck position

L = eng.kspluck(eng.double(164.82), nd, fs, e, B, A, p)
print(eng.size(L))
print(type(L))

# L = eng.cell2mat(eng.cell([eng.kspluck(eng.double(44.21), nd, fs, e, B, A, p),
# eng.kspluck(eng.double(44.21), nd, fs, e, B, A, p)]))

eng.audiowrite('mary_python.wav', L, fs, nargout=0)

