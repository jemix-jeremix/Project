# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:57:55 2016

@author: jéjé
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL
from matplotlib import cm

path = "images/multicolor.jpg"
im = PIL.Image.open(path)
R, G, B = im.split()
R = np.asarray(R, dtype = np.uint8)
G = np.asarray(G, dtype = np.uint8 )
B = np.asarray(B, dtype = np.uint8)

my_cmapR = plt.cm.get_cmap('Reds')
my_cmapG = plt.cm.get_cmap('Greens')
my_cmapB = plt.cm.get_cmap('Blues')

Z = R
Zs = Z > 100


fig = plt.figure("mes images")
plt.clf()
ax = fig.add_subplot(3,3,1)
ax.set_title("Normal")
plt.imshow(im)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,2)
ax.set_title("Red")
plt.imshow(R, cmap = my_cmapR)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,3)
ax.set_title("Green")
plt.imshow(G, cmap = my_cmapG)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,4)
ax.set_title("Blue")
plt.imshow(B, cmap = my_cmapB)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,5)
ax.set_title("Yellow")
plt.imshow(B, cmap = cm.YlOrBr)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,6)
ax.set_title("seuil")
plt.imshow(Zs, cmap = cm.gray)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(3,3,7)
ax.set_title("gris")
plt.imshow(B, cmap = cm.gray)
plt.grid()
plt.colorbar()


ax = fig.add_subplot(3,3,8)
ax.set_title("Rotation")
plt.imshow(im.rotate(180,expand=1))
plt.grid()
plt.colorbar()

ax = fig.add_subplot(3,3,9)
ax.set_title("Histogramme R")
plt.hist(Z.flatten(), bins = 250)
plt.show()