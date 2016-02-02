# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 16:06:07 2016

@author: jéjé
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = np.linspace(0., 10000., 100000)
y = np.exp(-x / 10.) * np.sin(2.* np.pi * x)

fig = plt.figure("Animation !")
plt.clf()
line, = plt.plot([], [])
plt.grid()
plt.xlim(0., 100.)
plt.ylim(-1.,1.)
def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=0.0001, blit=True)

plt.show()