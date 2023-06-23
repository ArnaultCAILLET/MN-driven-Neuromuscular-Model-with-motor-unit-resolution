""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

ODE that defines the dynamics of MU active state, from an input concentration of CaTn (in Mols)

"""

import numpy as np
from scipy.integrate import odeint


def MU_active_state_func(d, dt, CaTn_concentration, l_M_norm, MU_type, Matrix_AP): 
        
    time_MU = np.arange(0, d, dt) #the ODEs are solved with a 0.1ms step. Time t is in seconds        

    coefs = [1.00*10**5 , 0.024,  270] #works best against F-F steady-state curves. TTP = 60ms. Half Relaxation Time (HRT) = 75ms
  
    def ODE(a, t):
        CaTn = CaTn_concentration[int(t/dt)]     
        d1, d2, d3 = coefs
        dadt = d1*CaTn - a/(d2+d3*CaTn)
        return dadt
    
    active_state = odeint(ODE, 0, time_MU, hmax=dt/2)

    return  active_state
