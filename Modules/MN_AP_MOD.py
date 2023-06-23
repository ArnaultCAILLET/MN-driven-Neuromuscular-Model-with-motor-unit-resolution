""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computes trains of MN Action Potentials (half sine waves) according to identified discharge times (Matrix_AP), that have a 1/2048Hz time precision

"""
import numpy as np
from is_t_a_firing_time_MOD import is_t_a_firing_time_func

def MN_AP_func(t, Matrix_AP, V_N = 90):
    chosen_precision = 10**-3 # has to be higher than the duration of the AP (7*10**-4)
    
    t_round=int(t/chosen_precision+10**-4)*chosen_precision #input t [s] in chosen precision. +10**-4 is to avoid numerical imprecision that would be problematic with future 'int' function
    
    firing_time = is_t_a_firing_time_func(t_round, Matrix_AP, chosen_precision) #checks whether t_round is (1) or is not (0) a firing time
    
    if firing_time==0: #if not, the membrane potential remains zero
        alpha=0
    
    elif firing_time == 1: #if it is, returns the value of the sine wave calculated at time t
        # print(t)
        sin_period=1.4*10**-3 # 2*0.7ms
        
        t_end_sine_wave = t_round + sin_period/2
        alpha=0
        if t<=t_end_sine_wave:
            alpha = np.sin(2*np.pi/sin_period*(t-t_round))            
    return V_N * alpha
