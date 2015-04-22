# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np




#calcule les dérivées en certains points du tableau de fonction fourni en entrée
#retourne un tableau 
def derivation(y,eps):
    n = y.shape
    deriv_val = np.array(n)
    for i in range(0,n[0]-1):
        deriv_val[i] = (y[i + eps] - y [i]) / eps
    return deriv_val


#intègre une fonction f sur [a,b] selon la subdivision n , en utilisant la méthode globale des rectangles à droite
#Attention la subdivision utilisée doit être régulière

def integration(f,a,b,n):
    h = (b - a)/n
    res = 0
    for i in range(1,n):
        res = res + f[a + i*h]

    return h*res



#calcule la longueur de l'arc donné par la courbe de la fonction f sur [a,b]
#integ designe une méthode d'intégration passée en paramètre
def longueur(y,a,b,integ,n):
    f = derivation(y,eps)
    for i in range(0,y.shape[0] - 1):
        f[i] = np.sqrt(1 + tab[i]**2)
    tab = integration(f,a,b,n)
    return tab
        
        
        
## tests
n = 4
g = np.array([1,2,3])
a = 0
b = 1
tab = integration(g,a,b,n)
print tab
