import numpy as np
import re
import matplotlib.pyplot as plt

def load_foil(file):
    f = open(file, 'r')
    matchline = lambda line: re.match(r"\s*([\d\.-]+)\s*([\d\.-]+)", line)
    extra  = [];    intra = []
    rextra = False; rintra = False
    for line in f:
        m = matchline(line)
        if (m != None) and not(rextra):
            rextra = True
        if (m != None) and rextra and not(rintra):
            extra.append(m.groups())
        if (m != None) and rextra and rintra:
            intra.append(m.groups())
        if (m == None) and rextra:
            rintra = True
    ex = np.array(map(lambda t: float(t[0]),extra))
    ey = np.array(map(lambda t: float(t[1]),extra))
    ix = np.array(map(lambda t: float(t[0]),intra))
    iy = np.array(map(lambda t: float(t[1]),intra))
    return(ex,ey,ix,iy)

def interpolation_derivative(abs,ord):
    """ Returns the second derivative for the points defined by (abs, ord). """
    N = abs.size
    Snder = np.zeros(N)
    M = np.zeros([N,N])
    P = np.zeros(N)
    M[0,0] = 1.0 
    M[N-1,N-1] = 1.0
    P[0] = 0.0
    P[N-1] = 0.0
    for i in range(1,N-1):
        M[i, i-1] = (abs[i] - abs[i-1])/6
        M[i, i] = (abs[i+1] - abs[i-1])/3
        M[i, i+1] = (abs[i+1] - abs[i])/6
        P[i] = (ord[i+1] -ord[i])/(abs[i+1] - abs[i]) - (ord[i] - ord[i-1])/(abs[i] - abs[i-1])
    Snder = np.linalg.solve(M, P)
    return Snder

def interpolation_next(abs,ord,Snder,x):
    """ Returns the interpolation of the points defined by (abs, ord) for the x point. """
    N = abs.size
    for i in range(0,N-1):
        if (abs[i] <= x) and (x < abs[i+1]):
            A = (abs[i+1] - x) / (abs[i+1] - abs[i])
            B = 1.0 - A
            tmp = (1.0/6.0) * (abs[i+1] - abs[i])**2 
            C = tmp *(A**3 - A) 
            D = tmp *(B**3 - B)
            return A*ord[i] + B*ord[i+1] + C*Snder[i] + D*Snder[i+1]
    if x >= abs[N-1]:
        return ord[N-1]
    else:
        return ord[0]


def interpolation_do(abs,ord):
    N = abs.size
    Snder = interpolation_derivative(abs,ord)
    return lambda x: interpolation_next(abs,ord,Snder,x)

