import numpy as np
from math import exp

def rbf_network_cython(double[:,:] X, double[:] beta, int theta):
    cdef int i,j,d,N,D
    cdef float r    

    N = X.shape[0]
    D = X.shape[1]
    cdef double[:] Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y