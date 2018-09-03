import numpy as np
import matplotlib.pyplot as plt

A = .8
N = 44100
f = 440
n = np.arange(N)
phi = 0
y = A * np.cos(2 * np.pi * f * n/N + phi)
plt.plot(y)
plt.axis([0,440,-1,1])
plt.xlabel('sample index')
plt.ylabel('amplitude')
plt.show();
from scipy.io.wavfile import write
write('sine_440_1sec.wav', 44100, y)
