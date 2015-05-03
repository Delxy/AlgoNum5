# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from load_foil import load_foil
from part1_print import separation
from integration import longueur

# TODO: modifier pour aller avec les deux parties précédentes.


# return a lambda which compute the Bernouilli law for a given lambda.
def f_lambda(L, f, min_or_max):
    return lambda x: (1-L)*f(x) + L*min_or_max*3


def algo(filename):
    # e = extrados
    # i = intrados
    #first, we need to parse the file which contain data.
    (ex, ey, ix, iy) = load_foil(filename)

    # 'pas' define the number of slices we use.
    pas = 1/0.05

    # this is the result matrix
    mat = np.eye(2*pas, ex.shape[0])


    #Upper side:
    h_max = np.amax(ey)
    f_upper = interp1d(ex, ey, kind = 'cubic')

    
    for j in np.arange(0,1, 1/pas):
        # We look at each slice
        f = f_lambda(j, f_upper, h_max)
        # Then we compute his length 
        size = longueur(f, 0, ex[ex.shape[0]-1], 0.1)
        # And we write the result. (Je ne suis pas sure de ça, a verifier.
        for k in range(0,ex.shape[0]):
            mat[j*pas,k] = .5 *1000* (size * f(ex[k]))**2

    # Lower side:
    h_min = np.amin(iy)
    f_lower = interp1d(ix, iy, kind = 'cubic')
    for j in np.arange(0,1,1/pas):
        f = f_lambda(j, f_lower, h_min)
        size = longueur(f, 0, ix[ix.shape[0]-1], 0.1)
        print(size)
        for k in range(0, ex.shape[0]):
            mat[j*pas + pas,k] = .5 * 1000 *(size * f(ix[k]))**2
           

    # It displays the pressure map (ca ne focntionne pas encore.)
    
    plt.imshow(mat) 
    plt.show()

    

algo("DU84132V.DAT.txt")
