""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Description of the ODE that models the dynamics of MU action potentials

"""

from MN_AP_MOD import MN_AP_func

def MU_AP_ODE_func(t, dt, Matrix_AP, beta, dbetadt):
    c_4, c_5, c_6 = 2*10**4, 5*10**7, 9*10**7
    DDbetaDDt=c_6*MN_AP_func(t, Matrix_AP)-c_5*beta-c_4*dbetadt+10**-50
    return  DDbetaDDt