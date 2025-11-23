# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 17:09:15 2025

@author: apmil
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,101)
y = x**2
plt.plot(x,y,'sr')

#%% 

y2 = np.sin(x)
plt.plot(x,y2)

plt.savefig('C:/Users/apmil/Work/Fisica_Computacional_2425/new/test1.png', 
            dpi=300)
plt.show()

