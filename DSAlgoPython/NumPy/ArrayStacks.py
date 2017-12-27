#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:26:25 2017

@author: apple
"""

import numpy as np

array1 = np.array(range(100))

array2 = np.array(range(100,200))


array3 = np.array(range(300,400))



array4 = np.array(range(400,500))


#lprint(array1)


arr_stk = np.stack((array1,array2,array3,array4),axis = 1)
arr_stk2 = np.stack((array1,array2,array3,array4),axis = 0)
print(arr_stk
      )


print(arr_stk2)