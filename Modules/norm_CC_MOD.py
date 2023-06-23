""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

This function computes a normalized common control out of a list of MN discharge times

"""

import numpy as np
from CST_MOD import CST_func
from But_filter_MOD import But_filter_func

def norm_CC_func(N_MN, time, disch_times, plateau_time1, plateau_time2, fs, unit):
    Binary_matrix, CST=CST_func(N_MN, time, disch_times, unit) # Compute cumulative spike train
    common_control= But_filter_func(4, CST) # Filters the CST --> common control
    norm_CC = common_control / np.mean(common_control[int(plateau_time1*fs): int(plateau_time2*fs)]) # Normalizing
    return norm_CC
