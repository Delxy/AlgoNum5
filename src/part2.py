# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

## ------- Part 2 ------##
# Computing the length of the curve:
# The aim is to calculate the length of the curve by integrating a function in an interval with a given step h
# We worked in three steps: computing the derivation, then three integration methods, and finally computing the lentgh thanks to the formula



def derivation(f, a, b, n,eps):
    """It computes the derivative of the function f  in the range [a,b]. It uses the array deriv_value with contain f derivative values of n points.
    The input is a function and the output is an array."""
    
    step_deriv = (b-a)/n
    deriv_value = np.arange(a,b,step_deriv)
    for i in range(0,deriv_value.shape[0]): # We use 2 array, because one counts and deriv_value contain values where we want to derive.
        deriv_value[i] = (f(deriv_value[i] + eps) - f(deriv_value[i])) / eps
    return deriv_value

def right_rectangle_rule(f,a,b):
    """ Computes the global right rectangle rule. This function takes the array in ouput in range [a,b].The output is a number."""
    n = f.shape[0]
    h = (b - a)/n
    res = 0
    for i in np.arange(0, n):
        res = res + f[a + i*h]
    return h*res

def simpson_rule(f,a,b):
    """Computes the simpson rule"""
    n = f.shape[0]
    h = (b - a)/n
    
    res = (f[a]+f[b])/6
    som = 0
    for i in range(0,n):
        som = som + f[a + i*h]/3 +2*f[a + i*h + h/2]/3

    return h*(res + som)

def trapezoidal_rule(f,a,b):
    """ Computes the trapezoidal rule: takes in input a function f represented by an array, and two bounds a and b """
    n = f.shape[0]
    h = (b - a)/n

    res = (f[a] + f[b])/2
    for i in range(0,n):
        res = res + f[a + i*h]

    return res*h


def curve_length(integ_method,f,a,b,n):
    """ Computes the length of the curve f between a and b. n (subdivision) changes the accuracy."""
    deriv = derivation(f, a, b, n, 0.001) # It contains the derivative array of f.
    for i in np.arange(0, deriv.shape[0]): # Then we use the formula to compute the length of a curve
        deriv[i] = np.sqrt(1 + deriv[i]**2)
    res = integ_method(deriv,a,b) # integration using the method chosen in parameter
    return res




if __name__ == '__main__':
    print("Integration testing")
    def f(x):
        return x 
    assert(abs(curve_length(right_rectangle_rule,f,0,1,1000) - np.sqrt(2)) < 0.01)
    assert(abs(curve_length(trapezoidal_rule,f,0,1,1000) - np.sqrt(2)) < 0.01)
    assert(abs(curve_length(simpson_rule,f,0,1,1000) - np.sqrt(2)) < 0.01)
    
    def f(x):
        return 2
    assert(abs(curve_length(right_rectangle_rule,f,0,1,1000) - 1) < 0.01)
    assert(abs(curve_length(trapezoidal_rule,f,0,1,1000) - 1) < 0.01)
    assert(abs(curve_length(simpson_rule,f,0,1,1000) - 1) < 0.01)
    print("Integration testing done")

        
