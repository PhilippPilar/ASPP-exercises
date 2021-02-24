# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:35:19 2021

@author: Admin
"""
import numpy as np

#a)

p = np.array([[1.,2.,10],[3.,4.,20],[5.,6.,30],[7.,8.,40]])
p = (p.T/p[:,2]).T
print('a:\n',p)

#b)

b = np.random.rand(3,3)
print('b:\n',b)
bdiag = b[[0,1,2],[0,1,2]]
print('bdiag:\n',bdiag)

#c)
c = np.random.rand(10,3)
print('c:\n',c)
i = np.argmin(np.abs(c-0.75),axis = 1)
print('ci:\n',i)
#%%
#d)
print('d:')
x = np.empty((10,8,6))

idx0 = np.zeros((3,8)).astype(int)
idx1 = np.zeros((3,1)).astype(int)
idx2 = np.zeros((1,1)).astype(int)

d = x[idx0,idx1,idx2]
#indexing applied sequentially from right to left -> shape should be (3,8)
print('shape:',d.shape)
#it is indeed

#%%
#e)
print('e:')
x = np.arange(12, dtype = np.int32).reshape((3,4))
print(x)
z = np.lib.stride_tricks.as_strided(x, shape=(2,3,2,2),strides=(16,4,16,4))
print(z)