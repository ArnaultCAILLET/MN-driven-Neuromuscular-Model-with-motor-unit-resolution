""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Description of the MU type- length-dependent ODE describing the dynamics of free Calcium concentration in the MUs
"""

def coef_CA(MU_type):
    if MU_type == 'fast':
        c_1, c_2, c_3= 2.4*10.**3,  4.3*10.**5, 0.9
    elif MU_type == 'slow':
        c_1, c_2, c_3 =2.5*10.**3, 1.5*10.**5, 0.4 
    return c_1, c_2, c_3

def Ca_l_amplitude_func(l_M_norm): 
    if l_M_norm <=1.0:
        amp=0.8
    elif l_M_norm <=1.15:
        amp = 0.8+1.33*(l_M_norm-1.0)
    elif l_M_norm <=1.3:
        amp=1.0
    else:
        amp = 1.0-0.6*(l_M_norm-1.3)
    return amp

def Ca_l_width_func(l_M_norm): 
    if l_M_norm <=1.15:
        width = 1.0
    else:
        width = (1.0-0.4*(l_M_norm-1.15))
    return width

def MU_free_Ca_ODE_func(t, l_M_norm, MU_type, beta, gamma,  dgammadt):
    c_1, c_2, c_3 = coef_CA(MU_type) 

    amp=Ca_l_amplitude_func(l_M_norm) #impact of l_M_norm on Ca amplitude
    width=Ca_l_width_func(l_M_norm) #impact of l_M_norm on Ca half-width
    
    DDgammaDDt = c_3*beta - 1/amp*(c_1*dgammadt+width*c_2*gamma)
    return DDgammaDDt