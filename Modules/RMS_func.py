# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:38:36 2021

@author: caill
"""

import numpy as np

def RMS_func(arr_exp, arr_simul):
    diff= arr_exp-arr_simul
    return np.sqrt(np.mean(diff**2))