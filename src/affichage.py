# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from part1 import *

def display(ex, ey, ix, iy):
    """ This function displays extrados and intrados"""
    extrados = interpolation_do(ex,ey)
    intrados = interpolation_do(ix,iy)
    points = 200
    min1 = min(ex)
    max1 = max(ex)
    x = util(min1, max1, points)
    extrados_display = np.zeros(points)
    intrados_display = np.zeros(points)

    for i in range(0, points):
        extrados_display[i] = extrados(x[i])
        intrados_display[i] = intrados(x[i])

    plt.plot(x, extrados_display, 'r', label="Extrados interpolation", color = 'blue')
    plt.plot(ex, ey, 'r+', label="Extrados points", color='blue')
    plt.plot(x, intrados_display, 'g', label="Intrados interpolation", color='red')
    plt.plot(ix, iy, 'g+', label="Intrados points", color='red')
    plt.xlabel("Absciss")
    plt.ylabel("Ordinate")
    plt.title("Cubic spline interpolation of the airfoil")
    plt.axis([min1,max1,3*np.amin(iy),3*np.amax(ey)]) 
    plt.legend()
    plt.show()
    
def util(min1, max1, points):
    pitch = (max1 - min1) / points
    x = np.arange(min1, max1, pitch)
    return x 
