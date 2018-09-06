import numpy as np
import matplotlib.pyplot as plt
import math

vmax = 20
samp_rate = 1000
altura = 1
length = 1
heigth = 1
xi = 0
xf = 10
delta = 1
value = 1

source = lambda vmax,samp_rate: np.linspace(-vmax,vmax,samp_rate)
seno = [math.sin(x) for x in source(vmax,samp_rate)]
coseno = [math.cos(x) for x in source(vmax,samp_rate)]
triang = lambda altura: [max(altura-abs(x),0) for x in source(vmax,samp_rate)] 
square = lambda length, heigth: [0 if x < -length/2 or x > length/2
                                      else heigth for x in source(vmax,samp_rate)]
sinx = lambda: [math.sin(x)/x for x in source(vmax,samp_rate)]
"""grow_exp = lambda xi,xf: np.append([0 for x in np.linspace(-vmax,
                                                        xi,
                                                        math.floor(
                                                            (vmax-xi)/samp_rate))],
                                   [math.exp(x) for x in np.linspace(xi,
                                                                  xf,
                                                                  math.floor(
                                                                      (xf-xi)/samp_rate))],
                                   [0 for x in np.linspace(xf,
                                                        vmax,
                                                        math.floor(
                                                            (vmax-xf)/samp_rate))]
)
dec_exp = lambda xi,xf: [x for x in reversed(grow_exp(xi,xf))]
"""
dirac = lambda delta: [0 if x != samp_rate/2 else delta for x in range(samp_rate)]  
step = lambda value: [0 if x < 0 else value for x in source(vmax,samp_rate)]

#f_entrada = [seno, square(length,heigth), triang(altura)]
#f_transf = [dec_exp(xi,xf),grow_exp(xi,xf),dirac(delta),step(value),sinx]

plt.plot(source(vmax,samp_rate),step(value))
plt.xlabel('sample index')
plt.ylabel('amplitude')
plt.show();
