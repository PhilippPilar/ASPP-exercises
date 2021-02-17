# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:22:10 2021

@author: Admin
"""

import numpy as np

#a)
a = np.zeros(10)
a[4] = 1
print('a:\n',a)

#b)
b = np.arange(10,50)
print('b:',b)

#c)
c = b[::-1]
print('c:\n',c)

#d)
d = np.arange(0,9)
d = d.reshape([3,3])
print('d:\n',d)

#e)
e = np.array([1,2,0,0,4,0])
ei = np.where(e == 0)
print('e:\n',e)
print('e-0ind:\n',ei[0])

#f)
f = np.random.rand(30)
fmean = np.mean(f)
print('f:\n',f)
print('fmean:\n',fmean)

#g)
def get_g(dg0,dg1):
    g = np.zeros([dg0,dg1])
    g[[0,dg0-1],:] = 1
    g[:,[0,dg1-1]] = 1
    return g

dg0 = 11
dg1 = 7
g = get_g(dg0,dg1)
print('g:\n',g)

#h)
h = np.zeros([8,8])
h[::2,::2]=1
h[1::2,1::2]=1
print('h:\n',h)

#i)
i0 = [[1,0],[0,1]]
i = np.tile(i0,(4,4))
print('i:\n',i)

#j)
Z = np.arange(11)
Z[np.where((Z>2) & (Z<9))] *= -1
print('j:\n',Z)

#k)
Z = np.random.random(10)
Z = np.sort(Z)
print('k:\n',Z)

#l)
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = bool(int(np.mean(A==B)))
print('l:\n',equal)

#m)
print('m:')
Z = np.arange(10, dtype = np.int32)
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)

#n)
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print('n:\n',D)







