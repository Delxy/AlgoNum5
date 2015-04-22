# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np




### Calcule les dérivées en certains points du tableau de fonction fourni en entrée
# retourne un tableau 
def derivation(y,eps):
    n = y.shape
    deriv_val = np.array(n)
    for i in range(0,n[0]-1):
        deriv_val[i] = (y[i + eps] - y [i]) / eps
    return deriv_val


###### Methodes d'integration disponibles pour les tests #####


#1# méthode globale des rectangles à droite

# intègre une fonction f sur [a,b] selon la subdivision n , en utilisant la 
# Attention la subdivision utilisée doit être régulière

def integration_globale_a_droite(f,a,b,n):
    h = (b - a)/n
    res = 0
    for i in range(0,n):
        res = res + f[a + i*h]

    return h*res




#2# Methode du point milieu

#3# Methode rectangle à gauche



#### Calcul de la longueur de l'arc donné par la courbe de la fonction f sur [a,b]

#integ designe une méthode d'intégration passée en paramètre
def longueur(y,a,b,n):
    f = derivation(y,eps)
    for i in range(0,y.shape[1] - 1):
        f[i] = np.sqrt(1 + f[i]**2)
    res = integration(f,a,b,n)
    return res 
        
        
        
## tests
n = 4
g = np.array([1,2,3])
a = 0
b = 1
tab = integration_globale_a_droite(g,a,b,n)
print tab


## tests longueur arc sur fonction constante

f = np.array([3,3,3,3,3,3,3,3,3])
print integration_globale_a_droite(f,0,1,10)
