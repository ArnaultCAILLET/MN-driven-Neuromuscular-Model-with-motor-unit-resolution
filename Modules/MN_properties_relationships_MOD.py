""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

From the literature (see manuscript), distribution of the MU torque recruitment threshold Fth (%MVC), normalized max iso forces F0MU, and normalized MU twitch forces across the TA MU pool

"""

def Fth_distrib_func(MN, MN_pop): 
    return 0.5052*(58.1*MN/MN_pop+120**((MN/MN_pop)**1.83)) 


def F0MU_norm_distrib_func(MN,  MN_pop): 
    return 7.86*10**-4*(3.0*MN/MN_pop+8.20**((MN/MN_pop)**5.29))   


def Ftw_norm_distrib_func(MN, muscle, MN_pop): 
    return 6.07*(4.52*MN/MN_pop+11.96**((MN/MN_pop)**4.66))    

    


