""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computation of the MU Action Potentials from input trains of MN Action Potentials
"""

import numpy as np
from scipy.integrate import odeint
from MU_AP_ODE_MOD import MU_AP_ODE_func

def MU_AP_func(d, dt,  Matrix_AP, integration_step, delay = 'y'): 
    if delay =='y':
        syn_delay, sarc_delay, tub_delay =  0.5*10**-3, 3.0*10**-3, 0.5*10**-3  #s
        MAP_delay = syn_delay + sarc_delay + tub_delay
    else: 
        MAP_delay = 0
        
    time_MU = np.arange(0, d, dt) #the ODEs are solved with a 0.1ms step. Time t is in seconds        
    
    def ODE(X, t):
        beta = X[0]
        dbetadt = X[1]
        DDbetaDDt=MU_AP_ODE_func(t-MAP_delay, dt, Matrix_AP, beta, dbetadt) 
        return dbetadt, DDbetaDDt
    
    X = odeint(ODE, [0, 0], time_MU, hmax=integration_step)
    MU_AP_train = X[:,0]
    
    Vmax_factor = 0.85 # AP amplitude decreases in the t-tubules    
    return Vmax_factor * MU_AP_train
