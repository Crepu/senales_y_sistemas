import numpy as np
import matplotlib.pyplot as plt
import math

vmax = 200
samp_rate = 44100
base = 20
length = 20
heigth = 20
xi = -10
xf = 10
delta = 10
value = 1

source = lambda vmax,samp_rate: np.linspace(-vmax,vmax,samp_rate)
seno = [math.sin(x) for x in source(vmax,samp_rate)]
coseno = [math.cos(x) for x in source(vmax,samp_rate)]
triang = lambda base: [max(base/2-abs(x),0) for x in source(vmax,samp_rate)] 
square = lambda length, heigth: [0 if x < -length/2 or x > length/2
                                      else heigth for x in source(vmax,samp_rate)]
sinx = lambda: [math.sin(x)/x for x in source]
grow_exp = lambda xi,xf: [math.exp(x) for x in np.linspace(xi,xf,samp_rate)]
dec_exp = lambda xi,xf: [x for x in reversed(grow_exp(xi,xf))]
dirac = lambda delta: [0 if x != 0 else delta for x in source(vmax,samp_rate)] 
step = lambda value: [0 if x < 0 else value for x in source(vmax,samp_rate)]

f_entrada = [seno, square(length,heigth), triang(base)]
f_transf = [dec_exp(xi,xf),grow_exp(xi,xf),dirac(delta),step(value),sinx]

plt.plot(source(vmax,samp_rate),seno, coseno, triang(base),square(length, heigth))
plt.xlabel('sample index')
plt.ylabel('amplitude')
plt.show();
