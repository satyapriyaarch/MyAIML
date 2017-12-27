#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:25:43 2017

@author: apple
"""

import numpy as np


arr = np.arange(100,dtype = float).reshape(10,10)


'''
print(arr[1])

print(arr[0][4])

print(arr[0,4])
'''


#Syntax: start:stop:step with start (default 0) stop (default last) step (default 1)


print(arr[:7:2,2:9:3])

print( arr[:,:]) # all rows all column


print(arr [0,1:9:3])



