""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computation of the free Calcium concentration (in Mols) in the MUs from an input MU action potential (in V)
"""


import numpy as np
from scipy.integrate import odeint
from MU_free_Ca_ODE_MOD import MU_free_Ca_ODE_func

def MU_free_Ca_func(d, dt, MU_AP_train, l_M_norm, MU_type, Matrix_AP, delay = 'y'): 

    if delay =='y':
        CA_delay = 2.1*10**-3
    else: 
        CA_delay = 0
        
    time_MU = np.arange(0, d, dt) #the ODEs are solved with a 0.1ms step. Time t is in seconds        
        
    def ODE(X, t):
        gamma = X[0]
        dgammadt = X[1]
        beta = MU_AP_train[max(int((t-CA_delay)/dt), 0)]
        DDgammaDDt=MU_free_Ca_ODE_func(t-CA_delay, l_M_norm, MU_type, beta, gamma,  dgammadt)    
        return dgammadt, DDgammaDDt
    
    X = odeint(ODE, [0, 0], time_MU, hmax=dt)
    free_Ca_concentration = X[:,0]
    free_Ca_concentration[np.argwhere(free_Ca_concentration<0)]=0 # avoiding negligible negative values 

    return  free_Ca_concentration