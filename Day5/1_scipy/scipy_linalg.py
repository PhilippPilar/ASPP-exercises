# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:07:32 2021

@author: Admin
"""

import numpy as np
import scipy.linalg as linalg

#a)-d):
print('a-d:\n')

A = np.arange(1,10).reshape([3,3])
b = np.array([1,2,3])



x = linalg.solve(A,b)
print(x)
print(A@x,b)

offset = + 1e-9*np.eye(3) #to avoid ill-conditioningx = linalg.solve(A,b)
x = linalg.solve(A+offset,b)
print(x)
print(A@x,b)

#e)
print('e:\n')
B = np.random.rand(3,3)*2
X = linalg.solve(A,B)
print('X:',X)
print('AX:',A@X)
print('B:',B)

#f)
print('f:\n')
l,v = linalg.eig(A)
print('eigenvalues:\n',l)
print('eigenvectors:\n',v)

#g)
print('g:\n')
Ainv = linalg.inv(A)
Adet = linalg.det(A)
print('inv(A):\n',Ainv)
print('det(A):\n',Adet)

#h)
print('h:\n')
print('norm-1:',linalg.norm(A,1))
print('norm-2:',linalg.norm(A,2))
print('norm-inf:',linalg.norm(A,np.inf))