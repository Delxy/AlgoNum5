import numpy as np;
import re; # regexp
import matplotlib.pyplot as ma;
from scipy.interpolate import interp1d
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


def separation(k, ex, ey, ix, iy):
    
    if k == 1:
        intra1 = [0.0]*(ex[0])
        for i in range(0, np.int(ex[0])):
            intra1[i] = ix[i]
        #print intra1
        return intra1
    if k == 2:
        intra2 = [0.0]*(ey[0])
        for i in range(0, np.int(ey[0])):
            intra2[i] = ix[i+ex[0]]
        #print intra2
        return intra2
    if k == 3:
        extra1 = [0.0]*(ex[0])
        for i in range(0, np.int(ex[0])):
            extra1[i] = iy[i]
       # print extra1
        return extra1
    if k == 4:
        extra2 = [0.0]*(ey[0])
        for i in range(0, np.int(ey[0])):
            extra2[i] = iy[i+ex[0]]
       # print extra2
        return extra2



# f1 = interp1d(separation(1), separation(3), kind = 'cubic')
# f2 = interp1d(separation(2), separation(4), kind = 'cubic')
# plt.plot(separation(1), separation(3), 'o', separation(1), f1(separation(1)), '-', separation(2), separation(4), 'x', separation(2), f2(separation(2)), '--')
# plt.legend(['data1', 'cubicup', 'data2', 'cubicdown'], loc = 'best')
# plt.show()




