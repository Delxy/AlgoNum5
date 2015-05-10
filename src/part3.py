# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import part1 as part1
import integration as itg


def f_lambda(L, f, min_or_max):
    """This function returns a lambda which describes the airflow arround f for a given lambda L. If f describe the extrados, the max value of f should be given (and the min value for the intrados"""
    return lambda x: (1-L)*f(x) + L*min_or_max*3

def transfer(value, h_max, h_min, acc):
    """This fonction returns a value which is modified to be well save in the matrix"""
    if(value > 0):
        return -int(value*acc-3*acc*h_min)
    else:
        return int (-value*acc+3*acc*h_min)
    return value


def pressure_map(filename,nb_slice,integ_methode):
    """ This compute compute the pressure map around an airfoil, which is in the file filename with the given slice number. """
    # e = extrados
    # i = intrados
    #first, we need to parse the file which contain data.
    (ex, ey, ix, iy) = part1.load_foil(filename)

    # h_max and h_min are the max value and min value of the extrados and the intrados
    h_max = np.amax(ey)
    h_min = np.amin(iy)

    # Here we build the result matrix, with an accuracy which allow us to store more different value, then the pressure map is closer to the reality.
    accuracy = nb_slice
    matrix_length = int(3* accuracy *(h_max-h_min))
    matrix = np.zeros([matrix_length, matrix_length])
    
    # We interpolate the two curves.
    f_upper = part1.interpolation_do(ex, ey)
    f_lower = part1.interpolation_do(ix, iy)

    # Curves are interpolated, so we can chose all value for x in the interpolation range.
    x_values = np.arange(0, ex[ex.shape[0]-1], 1/matrix_length)
    
    # The first loop is for all slice.
    for j in np.arange(0,1, (1.0/nb_slice)):
    
        # EXTRADOS
        # We compute the size of each slice
        f = f_lambda(j, f_upper, h_max)
        
        size = itg.longueur(integ_methode,f, 0, 1, 10)

        # Then we put this value in each point of the airflow.
        for x in range(0, matrix_length):
            res = f(x_values[x])
            matrix[x, transfer(res, h_max, h_min, accuracy)] = 500*(size**2)

        # INTRADOS
        f = f_lambda(j, f_lower, h_min)
        size = itg.longueur(integ_methode,f, 0, 1, 10)

        for x in range(0, matrix_length):    
            res = f(x_values[x])
            matrix[x, transfer(res, h_max, h_min, accuracy)] = 500*(size**2)

    
    # Then the slice are displayed and the pressure map afterward.
    part1.display(ex, ey, ix, iy)
    plt.imshow(np.transpose(matrix), interpolation = 'nearest')
    plt.show()

    

pressure_map("DU84132V.DAT.txt", 100, itg.integration_globale_a_droite)
#pressure_map("HS1606.DAT", 100, itg.integration_globale_a_droite)