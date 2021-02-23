# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:37:12 2021

@author: Admin
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


#a)

fig, ax = plt.subplots(1,3)
pP = st.poisson(5)
x = np.arange(0,10)
ax[0].vlines(x,0,pP.pmf(x))

ax[1].plot(pP.cdf(x))

pP_samples = pP.rvs(1000)
ax[2].hist(pP_samples,11)

ax[0].title.set_text('pmf')
ax[1].title.set_text('cdf')
ax[2].title.set_text('hist')

fig.suptitle('Poisson(5)-distribution')


#%%
#b)
fig2, ax2 = plt.subplots(1,3)
pN = st.norm(0,1)
x = np.linspace(-10,10,201)
ax2[0].plot(x,pN.pdf(x))
ax2[1].plot(x,pN.cdf(x))
pN_samples = pN.rvs(1000)
ax2[2].hist(pN_samples,51)

ax2[0].title.set_text('pdf')
ax2[1].title.set_text('cdf')
ax2[2].title.set_text('hist')

fig2.suptitle('Normal(0,2)-distribution')


#%%
#c)
Nc = 100
s1 = pP.rvs(Nc)
s2 = pN.rvs(Nc)
s3 = pP.rvs(Nc)
s4 = pN.rvs(Nc)


s12 = st.ttest_ind(s1,s2)
s13 = st.ttest_ind(s1,s3)
s24 = st.ttest_ind(s2,s4)
print('reject H0 (equal averages) for p<0.1:')
print('sP=sN:',s12)
print('sP=sP:',s13)
print('sN=sN:',s24)











