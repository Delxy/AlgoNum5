# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np





def derivation(f, a, b, n,eps):
    """It computes the derivative of the function f  in the range [a,b]. It uses the array deriv_value with contain f derivative values of n points.
    The input is a function and the output is an array."""
    
    step_deriv = (b-a)/n
    deriv_value = np.arange(a,b,step_deriv)
    for i in range(0,deriv_value.shape[0]): # We use 2 array, because one counts and deriv_value contain values where we want to derive.
        deriv_value[i] = (f(deriv_value[i] + eps) - f(deriv_value[i])) / eps
    return deriv_value


def derivation_1(f, x, eps):
    return (f(x + eps) - f(x)) / eps

#1# méthode globale des rectangles à droite
def integration_globale_a_droite(f,a,b):
    """ This function 'intègre' the array in ouput in range [a,b].The output is a number."""
    n = f.shape[0]
    h = (b - a)/n
    res = 0
    for i in np.arange(0, n):
        res = res + f[a + i*h]
    return h*res

#2# Methode du point milieu
def simpson(f,a,b):
    n = f.shape[0]
    h = (b - a)/n
    
    res = (f[a]+f[b])/6
    som = 0
    for i in range(0,n):
        som = som + f[a + i*h]/3 +2*f[a + i*h + h/2]/3

    return h*(res + som)
    
#3# Methode des trapèzes
def trapeze(f,a,b):
    n = f.shape[0]
    h = (b - a)/n

    res = (f[a] + f[b])/2
    for i in range(0,n):
        res = res + f[a + i*h]

    return res*h


def longueur(integ_methode,f,a,b,n):
    """ It computes the length of the curve f between a and b. n change the accuracy."""
    deriv = derivation(f, a, b, n, 0.001) # It contains the derivative array of f.
    for i in np.arange(0, deriv.shape[0]): # Then we use the formula to compute the length of a curve
        deriv[i] = np.sqrt(1 + deriv[i]**2)
    res = integ_methode(deriv,a,b) # To conclude we 'intègrons'
    return res

# exemple d'utilisation 


if __name__ == '__main__':
    def f(x):
        return np.log(x)
    
        out = longueur(integration_globale_a_droite,f,1,30,10)
        print out
        
        out = longueur(trapeze,f,1,30,10)
        print out

        out = longueur(simpson,f,1,30,10)
        print out

        
