# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np



### Calcule les dérivées en certains points du tableau de fonction fourni en entrée
# retourne un tableau 
def derivation(f, a, b, n,eps):
    deriv_val = np.eye((b-a)/n)
    for i in np.arange(a,b,n):
        deriv_val[i] = (f(i + eps) - f(i)) / eps
    return deriv_val


###### Methodes d'integration disponibles pour les tests #####


#1# méthode globale des rectangles à droite

# intègre une fonction f sur [a,b] selon la subdivision n , en utilisant la 
# Attention la subdivision utilisée doit être régulière

def integration_globale_a_droite(f,a,b):
    n = f.shape[0]
    h = (b - a)/n
    res = 0
    for i in range(0,n):
        res = res + f[a + i*h]

    return h*res




#2# Methode du point milieu

#3# Methode rectangle à gauche



#### Calcul de la longueur de l'arc donné par la courbe de la fonction f sur [a,b]

#integ designe une méthode d'intégration passée en paramètre
def longueur(f,a,b,n):
    deriv = derivation(f, a, b, n, 0.01)
    for i in np.arange(a,b, n):
        deriv[i] = np.sqrt(1 + f(i)**2)
    res = integration_globale_a_droite(deriv,a,b)
    return res[0]
        
        
        
