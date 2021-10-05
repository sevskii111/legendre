import numpy as np
import scipy.special
import numpy.polynomial
import scipy.integrate as integrate


def solve(x, y, deg):
    c = numpy.polynomial.legendre.legfit(x, y, deg)
    ya = np.zeros_like(x)
    for j in range(deg + 1):
        p = scipy.special.legendre(j)
        ya += p(x) * c[j]
    l = np.linspace(0, len(c) - 1, len(c))
    cn = np.sqrt((2*l+1)/2)
    return ya, c / cn


def smart_solve(limits, f, deg, N=100):
    cs = list()
    degs = np.linspace(0, deg, deg + 1)
    scales = np.sqrt((2 * degs + 1) / 2)

    ya = np.zeros(N)
    for j in range(deg + 1):
        p = scipy.special.legendre(j)
        p *= scales[j]
        c = integrate.quad(lambda x: f(x) * p(x), limits[0], limits[1])[0]
        cs.append(c)
        ya += c * p(np.linspace(limits[0], limits[1], N))

    return ya, cs
