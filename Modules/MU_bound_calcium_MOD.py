""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

ODE that defines the dynamics of CaTn concentration in the MUs (in Mols), from an input concentration of free Calcium (in Mols)

"""

import numpy as np
from scipy.integrate import odeint


def MU_bound_calcium_func(d, dt, free_Ca_concentration, l_M_norm, MU_type, Matrix_AP): 

    time_MU = np.arange(0, d, dt) #the ODEs are solved with a 0.1ms step. Time t is in seconds        

    if MU_type == 'fast':
        T = 3.8*10**-4 
        k1=0.1*10**13 
        k2 = 41 
    elif MU_type == 'slow':
        T = 17*10**-5 
        k1=0.6*10**13 
        k2 = 21 
    
    coefs = [T, k1, k2 ] 

    def ODE(delta, t):
        gamma = free_Ca_concentration[int(t/dt)]     
        T, k1, k2 = coefs
        ddeltadt = k1*T*gamma**2-(k1*gamma**2+k2)*delta #║Wexler 1997. See the equation in Baylor 1998. It is quite the same but not entirely. 
        return ddeltadt
    
    CaTn = odeint(ODE, 0, time_MU, hmax=dt/2)

    return  CaTn
