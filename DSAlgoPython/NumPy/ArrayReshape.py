#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:11:17 2017

@author: apple
"""


import numpy as np

array = np.arange(10 , dtype = float).reshape(2,5)

a_col = array[:, np.newaxis]

#print(a_col)
print(array)

arr_flt = array.ravel()
arr_flt[1] = 30

print(arr_flt)
print(array)


matrixx = np.matrix(array)


print(matrixx)





matrixy = matrixx.T

print(matrixy)
print(matrixx * matrixy)