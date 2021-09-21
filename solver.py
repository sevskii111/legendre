import numpy as np
import scipy.special
import numpy.polynomial


def solve(x, y, deg):
    c = numpy.polynomial.legendre.legfit(x, y, deg)
    ya = np.zeros_like(x)
    for j in range(deg + 1):
        p = scipy.special.legendre(j)
        ya += p(x) * c[j]
    return ya